from flask import render_template, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Role, Post, Comment, Dislike, Like, Category
from .. import db
from .forms import UpdateProfileForm


# homepage
@main.route('/')
# @login_required
def index():
    return render_template('index.html')


# profile page
@main.route('/profile/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    form = UpdateProfileForm()
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.about_me = form.about_me.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.about_me.data = user.about_me

    return render_template('profile/profile.html', user=user, form=form)

# update profile page


# @main.route('/update_profile/<username>', methods=['GET', 'POST'])
# @login_required
# def update_profile(username):
#     user = User.query.filter_by(username=username).first()
#     if user is None:
#         abort(404)
#     form = UpdateProfileForm()
#     if form.validate_on_submit():
#         user.email = form.email.data
#         user.username = form.username.data
#         user.about_me = form.about_me.data
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('.profile', username=user.username))
#     form.email.data = user.email
#     form.username.data = user.username
#     form.about_me.data = user.about_me
#     return render_template('profile/profile.html', form=form)
