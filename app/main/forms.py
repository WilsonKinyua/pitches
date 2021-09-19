from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import User
from wtforms import ValidationError

# update profile form class


class UpdateProfileForm(FlaskForm):
    name = StringField('Name', validators=[Required(), Length(1, 64)])
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    email = StringField('Email', validators=[
                        Required(), Length(1, 64), Email()])
    about_me = TextAreaField('About me', validators=[
                             Required(), Length(1, 100)])
    # profile_pic = FileField()
    # confirmed = BooleanField('Confirmed')
    # role = StringField('Role', validators=[Required()])
    # location = StringField('Location', validators=[Required(), Length(1, 64)])
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


# create a new pitch form class
# class PitchForm(FlaskForm):
#     title = StringField('Pitch Title', validators=[Required(), Length(1, 64)])
#     body = TextAreaField('Pitch Content', validators=[Required()])
#     submit = SubmitField('Submit')

# comment form class
class CommentForm(FlaskForm):
    body = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')


class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[Required(), Length(1, 64)])
    submit = SubmitField('Submit')
