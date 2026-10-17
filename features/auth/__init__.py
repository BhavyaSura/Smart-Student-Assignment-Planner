"""
features/auth/__init__.py -- the "front door" of the account feature.

Create account, sign in and sign out live here. This feature has NO
sidebar button (the student is signed out when they see these pages),
so there is no NAV below.
"""
from flask import Blueprint

# The group of account pages.
auth_bp = Blueprint('auth', __name__)

# Load the page files so their routes attach to the Blueprint above.
# (This line must stay BELOW the Blueprint line.)
from . import routes  # noqa: E402,F401
