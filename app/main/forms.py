from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import User
from wtforms import ValidationError

# update profile form class


class UpdateProfileForm(FlaskForm):
    email = StringField('Email', validators=[
                        Required(), Length(1, 64), Email()])
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    # confirmed = BooleanField('Confirmed')
    # role = StringField('Role', validators=[Required()])
    name = StringField('Name', validators=[Required(), Length(1, 64)])
    # location = StringField('Location', validators=[Required(), Length(1, 64)])
    about_me = StringField('About me', validators=[Required(), Length(1, 64)])
    submit = SubmitField('Update Profile')

    # def __init__(self, user, *args, **kwargs):
    #     super(UpdateProfileForm, self).__init__(*args, **kwargs)
    #     self.user = user

    # def validate_email(self, field):
    #     if field.data != self.user.email and User.query.filter_by(email=field.data).first():
    #         raise ValidationError('Email already registered.')

    # def validate_username(self, field):
    #     if field.data != self.user.username and User.query.filter_by(username=field.data).first():
    #         raise ValidationError('Username already in use.')
