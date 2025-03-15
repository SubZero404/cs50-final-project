from flask import Blueprint, render_template, redirect, url_for

views = Blueprint('views', __name__)
path = 'views/'


@views.route('/')
def index():
    return render_template('index.html')

@views.route('/detail')
def detail():
    return render_template(path + 'detail.html')

@views.route('/about')
def about():
    return render_template(path + 'about.html')

@views.route('/contact')
def contact():
    return render_template(path + 'contact.html')
