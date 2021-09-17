from flask import render_template, redirect, url_for, abort
from . import main
# from ..models import User, Role, Post, Comment, Dislike, Like, Category
# from .. import db


# homepage
@main.route('/')
def index():
    return render_template('index.html')
