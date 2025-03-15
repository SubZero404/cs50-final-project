from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required
from .forms import CategoryForm
from .models import Category
from slugify import slugify
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


@admin.route('/add_product')
@login_required
def addProduct():
    return render_template(path + 'addProduct.html')


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