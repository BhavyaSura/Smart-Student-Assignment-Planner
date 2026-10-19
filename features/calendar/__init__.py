"""
features/calendar/__init__.py -- the "front door" of the Calendar feature.

The Calendar feature (SSAP-19). Right now it is only an empty page
with a "coming soon" box. Build the real calendar in this folder.

This file does three things:
  1. Creates the feature's Blueprint (its group of web pages).
  2. Describes the feature's sidebar button (NAV).
  3. Loads the page files so their routes attach to the Blueprint.
"""
from flask import Blueprint

# 1. The group of pages. Every page file in this folder attaches to it.
calendar_bp = Blueprint('calendar', __name__)

# 2. The sidebar button. app.py reads this and draws the button for us.
#    label    = the words on the button
#    endpoint = the page the button opens (blueprint name + function name)
#    order    = where it sits in the menu (small numbers come first)
#    icon     = the picture, as an SVG path
NAV = {
    'label': 'Calendar',
    'endpoint': 'calendar.calendar',
    'order': 40,
    'icon': (
        'M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zM9 14H7v-2h2v2zm4 0h-2v-2h2v2zm4 0h-2v-2h2v2zm-8 4H7v-2h2v2zm4 0h-2v-2h2v2zm4 0h-2v-2h2v2z'
    ),
}

# 3. Load the page files so their routes attach to the Blueprint above.
#    (This line must stay BELOW the Blueprint line.)
from . import routes  # noqa: E402,F401
