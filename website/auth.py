from flask import Blueprint, render_template, redirect, flash, url_for
from .forms import RegistrationForm, LoginForm
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        # check user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered. Please log in.", "warning")

        if password == confirm_password:
            new_user = User()
            new_user.username = username
            new_user.email = email
            new_user.password = generate_password_hash(password)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Account Successfully created!', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            print(e)
            flash("An error occurred. Please try again.", "danger")
    
    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    return 'Logout Page'


# from flask import Blueprint, render_template, redirect, url_for, flash
# from .forms import RegistrationForm, LoginForm
# from .models import User  # Import your User model
# from flask_login import login_user, logout_user
# from werkzeug.security import generate_password_hash, check_password_hash

# auth = Blueprint('auth', __name__)

# @auth.route('/register', methods=["GET", "POST"])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         # Check if user already exists
#         existing_user = User.query.filter_by(email=form.email.data).first()
#         if existing_user:
#             flash("Email already registered. Please log in.", "warning")
#             return redirect(url_for('auth.login'))

#         # Create new user
#         new_user = User(
#             username=form.username.data,
#             email=form.email.data,
#             password=generate_password_hash(form.password.data)  # Hash password
#         )
#         db.session.add(new_user)
#         db.session.commit()

#         flash("Account created successfully! You can now log in.", "success")
#         return redirect(url_for('auth.login'))

#     return render_template('register.html', form=form)


# @auth.route('/login', methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter(
#             (User.username == form.login.data) | (User.email == form.login.data)
#         ).first()

#         if user and check_password_hash(user.password, form.password.data):
#             login_user(user)
#             flash("Login successful!", "success")
#             return redirect(url_for('main.dashboard'))  # Change 'main.dashboard' based on your app

#         flash("Login failed. Please check your username/email and password.", "danger")

#     return render_template('login.html', form=form)


# @auth.route('/logout')
# def logout():
#     logout_user()
#     flash("You have been logged out.", "info")
#     return redirect(url_for('auth.login'))
