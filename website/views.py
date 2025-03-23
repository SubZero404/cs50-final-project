from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from .models import Product, Category, Brand

views = Blueprint('views', __name__)
path = 'views/'


@views.route('/')
def index():
    items = Product.query.all()
    flash_sale_items = Product.query.filter_by(flash_sale=True).all()
    categories = Category.query.all()
    brands = Brand.query.all()
    return render_template('index.html', items=items, flash_sale_items=flash_sale_items, categories=categories, brands=brands)

@views.route('/detail')
def detail():
    return render_template(path + 'detail.html')

@views.route('/about')
def about():
    return render_template(path + 'about.html')

@views.route('/contact')
def contact():
    return render_template(path + 'contact.html')
