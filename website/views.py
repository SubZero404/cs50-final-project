from flask import Blueprint, jsonify, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from .models import Product, Category, Brand, Image, Cart
from . import db

views = Blueprint('views', __name__)
path = 'views/'


@views.route('/')
def index():
    items = Product.query.order_by(Product.created_at.desc()).limit(12).all()
    flash_sale_items = Product.query.filter_by(flash_sale=True).order_by(Product.created_at.desc()).limit(12).all()
    categories = Category.query.all()
    brands = Brand.query.all()

    return render_template('index.html', items=items, flash_sale_items=flash_sale_items, categories=categories, brands=brands, cart_count=get_cart_count())

@views.route('/view-product/<int:product_id>', methods=['GET', 'POST'])
def viewProduct(product_id):
    product = Product.query.get_or_404(product_id)
    images = Image.query.filter_by(product_id = product.id).all()
    return render_template(path + 'view_product.html', product=product, images=images, cart_count=get_cart_count())

@views.route('/about')
def about():
    return render_template(path + 'about.html')

@views.route('/contact')
def contact():
    return render_template(path + 'contact.html')

@views.route('/products')
def products():
    items = Product.query.order_by(Product.created_at.desc()).all()
    return render_template(path + 'all_product.html', items=items, cart_count=get_cart_count())

@views.route('/flash-sales')
def flashSales():
    flash_sale_items = Product.query.filter_by(flash_sale=True).order_by(Product.created_at.desc()).all()
    return render_template(path + 'all_flash_sale.html', flash_sale_items=flash_sale_items, cart_count=get_cart_count())

# Route for Category
@views.route('/category/<slug>')
def category(slug):
    category = Category.query.filter_by(slug=slug).first_or_404()
    items = Product.query.filter_by(category_id=category.id).all()
    return render_template(path + 'by_category.html', category=category, items=items, cart_count=get_cart_count())

# Route for Brand
@views.route('/brand/<slug>')
def brand(slug):
    brand = Brand.query.filter_by(slug=slug).first_or_404()
    items = Product.query.filter_by(brand_id=brand.id).all()
    return render_template(path + 'by_brand.html', brand=brand, items=items, cart_count=get_cart_count())

@views.route('/add-to-cart/<int:product_id>', methods=['GET','POST'])
@login_required
def addToCart(product_id):
    product = Product.query.get_or_404(product_id)
    quantity = request.form.get('quantity', type=int, default=1)
    cart_item = Cart.query.filter_by(user_id = current_user.id, product_id = product_id).first()

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = Cart(user_id = current_user.id, product_id = product_id, quantity = quantity)
        db.session.add(cart_item)

    db.session.commit()
    return jsonify({"message": "Product added to cart!"}), 200



@views.route('/cart')
@login_required
def cart(): 
    user = current_user

    cart_items = Cart.query.filter_by(user_id = user.id).all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render_template(path + 'cart.html', cart_items=cart_items, total_price=total_price)


@views.route('/update-cart/<int:item_id>', methods=['GET','POST'])
@login_required
def updateCart(item_id):
    quantity = request.get_json().get('quantity')
    cart_item = Cart.query.filter_by(id=item_id).first()
    print(quantity)
    if cart_item and quantity is not None:
        try:
            quantity = int(quantity)
            if quantity > 0:
                cart_item.quantity = quantity
                db.session.commit()
                return jsonify({'success': True, 'message': 'quantity updated successfully'})
            else:
                return jsonify({'success': False, 'message': 'Quantity must be greater than 0'})
        except ValueError:
            return jsonify({'success': False, 'message': 'Invalid quantity'})
    else:
        return jsonify({'success': False, 'message': 'Cart item not found'})
    

@views.route('/remove-from-cart/<int:item_id>', methods=['GET','POST'])
@login_required
def removeFromCart(item_id):
    cart_item = Cart.query.filter_by(id=item_id).first()
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Product removed from cart'})
    else:
        return jsonify({'success': False, 'message': 'Cart item not found'})
    



def get_cart_count():
    if current_user.is_authenticated:
        return Cart.query.filter_by(user_id=current_user.id).count()
    return 0  # Return 0 if the user is not logged in
