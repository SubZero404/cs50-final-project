from flask import Blueprint, render_template, redirect, flash, url_for
from .forms import RegistrationForm, LoginForm
from .models import User
from flask_login import login_user, logout_user, login_required
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
            flash("Email already registered. Please log in.", "danger")
        else:
            if password == confirm_password:
                new_user = User()
                new_user.username = username
                new_user.email = email
                new_user.password = password
                try:
                    db.session.add(new_user)
                    db.session.commit()
                    flash('Account Successfully created!', 'success')
                    return redirect(url_for('auth.login'))
                except Exception as e:
                    print(e)
                    flash("An error occurred. Please try again.", "danger")
            else:
                flash("password not match.", "danger")
    return render_template('register.html', form=form)


@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter(User.email == email).first()

        if user and check_password_hash(user.password_hash, password):
            if user.is_active:
                login_user(user)
                flash("Login successful!", "success")
                return redirect(url_for('admin.dashboard'))
            else:
                flash("Your account is inactive. Please contact support for assistance.", "danger")
        else:
            flash("Login failed. Please check your email and password.", "danger")


    return render_template('login.html', form=form)

@auth.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('auth.login'))
