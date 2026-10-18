import re
from flask import (
    Blueprint, render_template, request, redirect, url_for, session, flash
)
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

# All the account pages (create account, sign in, sign out) live here.
auth_bp = Blueprint('auth', __name__)

# A simple check that an email looks like name@something.com
EMAIL_PATTERN = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Lowercase the email so Bob@x.com and bob@x.com count as the same.
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        # Check the form one problem at a time. The first problem found
        # becomes the error message shown to the student.
        error = None
        if not email or not password or not confirm_password:
            error = 'Please fill out every field.'
        elif not EMAIL_PATTERN.match(email):
            error = 'Please enter a valid email address.'
        elif len(password) < 8:
            error = 'Password must be at least 8 characters.'
        elif password != confirm_password:
            error = 'Passwords do not match.'
        elif User.query.filter_by(email=email).first():
            error = 'That email is already registered.'

        if error:
            return render_template('register.html', error=error, email=email)

        # Save only the scrambled version of the password, never the real one.
        user = User(
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            # Rare case: someone registered this email a split second ago.
            db.session.rollback()
            return render_template(
                'register.html',
                error='That email is already registered.',
                email=email
            )

        flash('Account created! Please sign in.')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        user = User.query.filter_by(email=email).first()

        # Same message for a wrong email or a wrong password, so nobody
        # can use this page to find out which emails have accounts.
        if user is None or not check_password_hash(user.password_hash, password):
            return render_template(
                'login.html',
                error='Incorrect email or password.',
                email=email
            )

        # Start a fresh session, then remember who just signed in.
        session.clear()
        session['user_id'] = user.id
        return redirect(url_for('index'))

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    # Forget who was signed in, then go back to the sign-in page.
    session.clear()
    return redirect(url_for('auth.login'))


# Pages anyone can open without signing in. Everything else needs an account.
PUBLIC_PAGES = ('auth.login', 'auth.register', 'static')


@auth_bp.before_app_request
def require_sign_in():
    # This runs before EVERY page in the whole app, not just the account
    # pages. If you aren't signed in, it sends you to the Sign In page.
    user_id = session.get('user_id')

    # If the cookie points to an account that doesn't exist anymore (for
    # example after deleting planner.db), treat the person as signed out.
    if user_id is not None and db.session.get(User, user_id) is None:
        session.clear()
        user_id = None

    if(
        user_id is None
        and request.endpoint is not None
        and request.endpoint not in PUBLIC_PAGES
    ):
        return redirect(url_for('auth.login'))
