from flask import render_template, redirect, url_for, abort, flash, request
from . import main
from flask_login import login_required, current_user
from ..models import User, Role, Post, Comment, Dislike, Like, Category
from .. import db, photos
from .forms import UpdateProfileForm
from slugify import slugify

# homepage

def getAuthor(id):
    user = User.query.filter_by(id=id).first()
    return user


@main.route('/')
# @login_required
def index():
    """
        View root page function that returns the index page and its data
    """
    # get pitches with their author and category and display them on the index page in the newest order of creation
    pitches = Post.query.order_by(Post.timestamp.desc()).all()
    
    
    return render_template('index.html', pitches=pitches)


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
    form.name.data = user.name
    form.email.data = user.email
    form.username.data = user.username
    form.about_me.data = user.about_me

    # get all the posts of the current user with its category
    pitches = Post.get_posts_by_author(
        user.id).order_by(Post.timestamp.desc()).all()

    return render_template('profile/profile.html', user=user, form=form, pitches=pitches)


# update profile picture
@main.route('/update_profile_pic', methods=['POST'])
@login_required
def update_profile_pic():
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        current_user.profile_image = path
        db.session.commit()
    return redirect(url_for('.profile', username=current_user.username))


# create a new pitch
@main.route('/new_pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():

    title = request.args.get('title')
    user_id = request.args.get('user_id')
    category_id = request.args.get('category_id')
    body = request.args.get('body')

    # make a new slug from the title
    slug = slugify(title)
    # check if the slug already exists
    pitch = Post.query.filter_by(slug=slug).first()
    if pitch is not None:
        # if it exists, append a number to the slug
        slug = slugify(title) + '-' + str(pitch.id)

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        picture_path = path

    new_pitch = Post(
        title=title,
        body=body,
        user_id=user_id,
        category_id=category_id,
        slug=slug,
        # picture_path=picture_path
    )
    db.session.add(new_pitch)
    db.session.commit()
    flash('New pitch created successfully!', 'success')
    return redirect(url_for('.profile', username=current_user.username))
