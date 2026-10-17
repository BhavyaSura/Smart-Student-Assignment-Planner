"""
features/assignments/__init__.py -- the "front door" of the Assignments feature.

The Assignments feature: upcoming list, add, edit/details and delete.
All of its pages share ONE blueprint, so the sidebar button stays
highlighted on every one of them.

This file does three things:
  1. Creates the feature's Blueprint (its group of web pages).
  2. Describes the feature's sidebar button (NAV).
  3. Loads the page files so their routes attach to the Blueprint.
"""
from flask import Blueprint

# 1. The group of pages. Every page file in this folder attaches to it.
assignments_bp = Blueprint('assignments', __name__)

# 2. The sidebar button. app.py reads this and draws the button for us.
#    label    = the words on the button
#    endpoint = the page the button opens (blueprint name + function name)
#    order    = where it sits in the menu (small numbers come first)
#    icon     = the picture, as an SVG path
NAV = {
    'label': 'Assignments',
    'endpoint': 'assignments.upcoming_assignments',
    'order': 30,
    'icon': (
        'M19 3h-4.18C14.4 1.84 13.3 1 12 1s-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm2 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z'
    ),
}

# 3. Load the page files so their routes attach to the Blueprint above.
#    (This line must stay BELOW the Blueprint line.)
from . import upcoming, add, details, delete  # noqa: E402,F401
