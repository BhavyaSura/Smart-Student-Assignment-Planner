"""
features/progress/__init__.py -- the "front door" of the Progress feature.

The Progress feature (SSAP-9, built by Bhavya). It shows how many
assignments are Not Started, In Progress and Completed, plus an overall
completion bar.

This file does three things:
  1. Creates the feature's Blueprint (its group of web pages).
  2. Describes the feature's sidebar button (NAV).
  3. Loads the page files so their routes attach to the Blueprint.
"""
from flask import Blueprint

# 1. The group of pages. Every page file in this folder attaches to it.
# The page address starts with /assignment-progress (set by url_prefix).
progress_bp = Blueprint(
    'progress',
    __name__,
    url_prefix='/assignment-progress'
)

# 2. The sidebar button. app.py reads this and draws the button for us.
#    label    = the words on the button
#    endpoint = the page the button opens (blueprint name + function name)
#    order    = where it sits in the menu (small numbers come first)
#    icon     = the picture, as an SVG path
NAV = {
    'label': 'Progress',
    'endpoint': 'progress.assignment_progress',
    'order': 50,
    'icon': (
        'M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z'
    ),
}

# 3. Load the page files so their routes attach to the Blueprint above.
#    (This line must stay BELOW the Blueprint line.)
from . import routes  # noqa: E402,F401
