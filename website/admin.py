from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required
from .forms import CategoryForm, ProductForm
from .models import Category, Product, Image
from slugify import slugify
from werkzeug.utils import secure_filename
import random
import os
from . import db

admin = Blueprint('admin',__name__)
path = 'admin/'


@admin.route('/dashboard')
@login_required
def dashboard():
    return render_template(path + 'dashboard.html')


@admin.route('/product_lists')
@login_required
def productLists():
    return render_template(path + 'productLists.html')


@admin.route('/add-product', methods=['GET', 'POST'])
@login_required
def addProduct():
    form = ProductForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]

    if form.validate_on_submit():
        product_image = form.product_image.data
        product_image_name = generate_unique_filename(product_image.filename, 'product')
        product_image_dir = os.path.join('website','static', 'img', 'products')

        if not os.path.exists(product_image_dir):
            os.makedirs(product_image_dir)

        product_image_path = os.path.join(product_image_dir, product_image_name)
        product_image.save(product_image_path)

        new_product = Product(
            name = form.name.data,
            description = form.description.data,
            price = form.price.data,
            previous_price = form.previous_price.data,
            category_id = form.category_id.data,
            quantity = form.quantity.data,
            product_image = product_image_name,
            flash_sale = form.flash_sale.data  
        )

        db.session.add(new_product)
        db.session.commit()
        # save additional images
        for image_file in form.additional_images.data:
            image_name = generate_unique_filename(image_file.filename, 'additional')
            image_dir = os.path.join('website','static', 'img', 'products')

            if not os.path.exists(image_dir):
                os.makedirs(image_dir)

            image_path = os.path.join(image_dir, image_name)
            image_file.save(image_path)

            new_image = Image(product_id=new_product.id, image_url=image_name)
            db.session.add(new_image)
            db.session.commit()

        flash('Product added successfully', 'success')
        
        return redirect(url_for('admin.productLists'))
    
    return render_template(path + 'addProduct.html', form=form)


def generate_unique_filename(filename, category='NOCATEGORY'):
    secure_name = secure_filename(filename)
    random_number = random.randint(1000000, 9999999)
    unique_filename = f"{category.upper}_{random_number}{os.path.splitext(secure_name)[1]}"
    return unique_filename


@admin.route('/categories', methods=['GET', 'POST'])
@login_required
def manageCategory():
    form = CategoryForm()
    categories = Category.query.order_by(Category.created_at.desc()).all()

    #update & delete category
    if form.validate_on_submit():
        category_id = request.form.get("category_id")
        name = form.name.data
        slug = slugify(name)

        if category_id:
            category = Category.query.filter_by(id = category_id).first()
            category.name = name
            category.slug = slug
            db.session.commit()
            flash('Category updated successfully', 'success')
        else:
            existing_category = Category.query.filter_by(slug = slug).first()
            if existing_category:
                flash('Category already exists', 'danger')
            else:
                category = Category(name=name, slug=slug)
                db.session.add(category)
                db.session.commit()
                flash('Category added successfully', 'success')
        return redirect(url_for('admin.manageCategory'))
    
    return render_template(path + 'category.html', form=form, categories=categories)


@admin.route('/delete_category/<int:category_id>', methods=['GET', 'POST'])
@login_required
def deleteCategory(category_id):
    category = Category.query.filter_by(id=category_id).first()
    if category:
        db.session.delete(category)
        db.session.commit()
        flash('Category deleted successfully', 'success')
    else:
        flash('Category not found', 'warning')
    return redirect(url_for('admin.manageCategory'))