"""
features/progress/routes.py -- Progress: the home page of the Progress feature (empty for now).
"""
# SSAP-9 (Bhavya): replace this empty page with the Progress feature.
from flask import render_template
from . import progress_bp


@progress_bp.route('/progress')
def progress():
    # Empty for now. This page is the home of the Progress feature.
    return render_template('progress/home.html')
