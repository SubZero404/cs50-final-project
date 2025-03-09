from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

views = Blueprint('views', __name__)



@views.route('/')
@login_required
def index():
    return render_template('index.html')

@views.route('/detail')
@login_required
def detail():
    return render_template('views/detail.html')

@views.route('/about')
@login_required
def about():
    return render_template('views/about.html')

@views.route('/contact')
@login_required
def contact():
    return render_template('views/contact.html')