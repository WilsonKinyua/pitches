from flask import render_template, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Role, Post, Comment, Dislike, Like, Category
# from .. import db


# homepage
@main.route('/')
# @login_required
def index():
    return render_template('index.html')


# profile page
@main.route('/profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('profile/profile.html', user=user)
