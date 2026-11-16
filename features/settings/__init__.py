"""
features/settings/__init__.py -- Settings feature.
"""
from flask import Blueprint
from flask_wtf.csrf import generate_csrf

# Create the Settings Blueprint.
settings_bp = Blueprint(
    'settings',
    __name__,
    url_prefix='/settings'
)

# Make CSRF tokens available to Settings templates.
@settings_bp.app_context_processor
def settings_csrf_context():
    return {'csrf_token': generate_csrf}


# Add Settings to the sidebar.
NAV = {
    'label': 'Settings',
    'endpoint': 'settings.settings',
    'order': 60,
    'icon': (
        'M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8zm8 4a8 8 0 0 1-.1 1.2l2 1.6-2 3.5-2.4-1a8 8 0 0 1-2 1.2l-.4 2.5h-4l-.4-2.5a8 8 0 0 1-2-1.2l-2.4 1-2-3.5 2-1.6a8 8 0 0 1 0-2.4l-2-1.6 2-3.5 2.4 1a8 8 0 0 1 2-1.2l.4-2.5h4l.4 2.5a8 8 0 0 1 2 1.2l2.4-1 2 3.5-2 1.6A8 8 0 0 1 20 12z'
    ),
}

# Register the Settings database model.
from . import models  # noqa: E402,F401

# Load the Settings routes.
from . import routes  # noqa: E402,F401