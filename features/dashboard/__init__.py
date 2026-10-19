"""
features/dashboard/__init__.py -- the "front door" of the Dashboard feature.

The Dashboard: the first page a student sees. It shows boxes
(summary, courses, schedule, mini calendar, upcoming) pulled from the
other features. Each box has its own small file in this folder.

This file does three things:
  1. Creates the feature's Blueprint (its group of web pages).
  2. Describes the feature's sidebar button (NAV).
  3. Loads the page files so their routes attach to the Blueprint.
"""
from flask import Blueprint

# 1. The group of pages. Every page file in this folder attaches to it.
dashboard_bp = Blueprint('dashboard', __name__)

# 2. The sidebar button. app.py reads this and draws the button for us.
#    label    = the words on the button
#    endpoint = the page the button opens (blueprint name + function name)
#    order    = where it sits in the menu (small numbers come first)
#    icon     = the picture, as an SVG path
NAV = {
    'label': 'Dashboard',
    'endpoint': 'dashboard.index',
    'order': 10,
    'icon': (
        'M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z'
    ),
}

# 3. Load the page files so their routes attach to the Blueprint above.
#    (This line must stay BELOW the Blueprint line.)
from . import routes  # noqa: E402,F401
