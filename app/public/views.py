from flask import Blueprint, render_template, redirect, session


blueprint = Blueprint('public', __name__, static_folder='../static')


@blueprint.route('/')
def home():
    """Home page."""
    return render_template('public/home.html')


@blueprint.route('/login')
def login():
    """Login page."""
    return render_template('public/login.html')


@blueprint.route('/register')
def register():
    """Register page."""
    return render_template('public/register.html')


@blueprint.route('/logout')
def logout():
    """logout link."""
    return redirect(url_for('home'))
