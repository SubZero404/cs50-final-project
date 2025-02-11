from flask import Blueprint, render_template

admin = Blueprint('admin',__name__)
path = 'admin/'

@admin.route('/dashboard')
def dashboard():
    return render_template(path + 'dashboard.html')