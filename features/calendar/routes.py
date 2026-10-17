"""
features/calendar/routes.py -- Calendar: the home page of the Calendar feature (empty for now).
"""
# SSAP-19: replace this empty page with the interactive calendar.
from flask import render_template
from . import calendar_bp


@calendar_bp.route('/calendar')
def calendar():
    # Empty for now. This page is the home of the Calendar feature.
    return render_template('calendar/home.html')
