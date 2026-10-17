"""
app.py -- starts the Smart Student Assignment Planner.

You should almost never need to edit this file. It does 3 jobs:
  1. Sets up Flask and the database.
  2. Finds every feature inside the "features" folder and turns it on.
  3. Builds the sidebar menu from what each feature says about itself.

Run the app with:  python app.py
"""
import importlib
import os
import pkgutil

from flask import Blueprint, Flask

import features
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'
# Flask uses this secret to protect the "you are signed in" cookie so
# nobody can fake it. For real use, set your own with the SECRET_KEY
# environment variable. The fallback below is only for local testing.
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-only-change-me')

db.init_app(app)  # connect the database to this app


# ------------------------------------------------------------------
# Turn on every feature automatically.
#
# Every folder inside "features" is one feature. This code opens each
# one, turns on its pages (its Blueprint), and reads its sidebar
# button (its NAV). Nobody has to come back to this file to add their
# feature -- that is what keeps us from causing merge conflicts here.
# ------------------------------------------------------------------
already_turned_on = []   # remembers blueprints so none is turned on twice
sidebar_buttons = []     # one entry per feature that has a menu button

for module_info in pkgutil.iter_modules(features.__path__):
    module = importlib.import_module(f'features.{module_info.name}')
    feature_blueprint = None

    # Turn on the feature's pages.
    for value in vars(module).values():
        if isinstance(value, Blueprint) and value not in already_turned_on:
            app.register_blueprint(value)
            already_turned_on.append(value)
            feature_blueprint = value

    # Remember the feature's menu button, if it has one.
    # (NAV lives in the feature's __init__.py. See features/README.md.)
    nav = getattr(module, 'NAV', None)
    if nav and feature_blueprint:
        sidebar_buttons.append({**nav, 'blueprint': feature_blueprint.name})

# Put the buttons in the order the features asked for (lowest first).
sidebar_buttons.sort(key=lambda button: button['order'])


@app.context_processor
def add_sidebar_buttons():
    """Make the list of menu buttons available to every template."""
    return {'nav_items': sidebar_buttons}


# Create the database tables. This runs AFTER the features are loaded
# so that tables from every feature's models are included.
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    # debug=True gives helpful error pages while you're building the app,
    # but it's not safe to leave on if this app ever ran on a real server --
    # it would let anyone run code through the browser. This line checks
    # for a setting called FLASK_DEBUG. If it isn't set, debug stays off,
    # so you have to turn it on on purpose while coding, e.g. in the
    # terminal: (Windows) $env:FLASK_DEBUG="True"  or (Mac/Linux) export FLASK_DEBUG=True
    debug_mode = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    app.run(debug=debug_mode)
