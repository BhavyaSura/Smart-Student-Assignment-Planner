"""
features/settings/routes.py -- Settings home page.
"""

from flask import render_template, session
from . import settings_bp


@settings_bp.route('/')
def settings():
    # Only signed-in students can access Settings.
    user_id = session.get('user_id')

    if user_id is None:
        from flask import redirect, url_for
        return redirect(url_for('auth.login'))

    return render_template('settings/home.html')

