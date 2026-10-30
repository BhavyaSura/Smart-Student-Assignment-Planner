"""
features/courses/__init__.py -- the "front door" of the Courses feature.

The Courses feature: a page of course squares plus the form that
adds a new course.

This file does three things:
  1. Creates the feature's Blueprint (its group of web pages).
  2. Describes the feature's sidebar button (NAV).
  3. Loads the page files so their routes attach to the Blueprint.
"""
from flask import Blueprint

# 1. The group of pages. Every page file in this folder attaches to it.
courses_bp = Blueprint('courses', __name__)

# 2. The sidebar button. app.py reads this and draws the button for us.
#    label    = the words on the button
#    endpoint = the page the button opens (blueprint name + function name)
#    order    = where it sits in the menu (small numbers come first)
#    icon     = the picture, as an SVG path
NAV = {
    'label': 'Courses',
    'endpoint': 'courses.courses',
    'order': 20,
    'icon': (
        'M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z'
    ),
}

# 3. Load the page files so their routes attach to the Blueprint above.
#    (This line must stay BELOW the Blueprint line.)
from . import routes, delete  # noqa: E402,F401
