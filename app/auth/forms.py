from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import User
from wtforms import ValidationError


# login form
class LoginForm(FlaskForm):
    """
    Login form
    """
    email = StringField('Email', validators=[
                        Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')


# register form
class RegistrationForm(FlaskForm):
    """
     class that defines the registration form
    """
    name = StringField('Name', validators=[Required(), Length(1, 64)])
    email = StringField('Email', validators=[
                        Required(), Length(1, 64), Email()])
    username = StringField('Username', validators=[
                           Required(), Length(1, 64)])
    password = PasswordField('Password', validators=[
                             Required(), EqualTo('confirm_password', message='Passwords must match.')])
    confirm_password = PasswordField(
        'Confirm password', validators=[Required()])
    submit = SubmitField('Create Account')

    def check_email_exist(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered. Please Login')

    def check_username_exist(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exist.')
