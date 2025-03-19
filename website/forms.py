from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, TextAreaField, FloatField, SelectField, FileField, MultipleFileField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange
from flask_wtf.file import FileAllowed

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    submit = SubmitField('Login')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired(), Length(min=2, max=20)])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=2, max=20)])
    save =SubmitField('Save')

class CategoryForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Category', validators=[DataRequired(), Length(min=2, max=64)]) 
    submit = SubmitField('Save')

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired(), Length(min=2, max=64)])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0)])
    previous_price = FloatField('Previous Price', validators=[DataRequired(), NumberRange(min=0)])
    category_id = SelectField('Category', coerce=int, validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=0)])
    product_image = FileField('Product Image', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    flash_sale = BooleanField('Flash Sale')
    additional_images = MultipleFileField('Additional Images', render_kw={"multiple": True}, validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('submit')