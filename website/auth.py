from flask import Blueprint, render_template
from .forms import RegistrationForm, LoginForm

auth = Blueprint('auth',__name__)

@auth.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)

@auth.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    return 'Logout Page'