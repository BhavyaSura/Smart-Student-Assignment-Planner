from flask import Flask, render_template, Blueprint
from models import db
import os
import importlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'
# Flask uses this secret to protect the "you are signed in" cookie so
# nobody can fake it. For real use, set your own with the SECRET_KEY
# environment variable. The fallback below is only for local testing.
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-only-change-me')

db.init_app(app)  # connect the database to this app

with app.app_context():
    db.create_all()  # create the database tables if they don't exist yet

# --- This part automatically turns on everyone's features ---
# It looks inside the "features" folder, opens every file in there,
# and turns on any feature it finds. This means nobody has to come
# back to this file and add a line for their feature -- it just
# works as soon as their file is in the folder. That's what keeps
# us from all editing this same file and causing merge conflicts.
features_dir = os.path.join(os.path.dirname(__file__), 'features')
for filename in os.listdir(features_dir):
    if filename.endswith('.py') and filename != '__init__.py':
        module = importlib.import_module(f'features.{filename[:-3]}')
        for value in vars(module).values():
            if isinstance(value, Blueprint):
                app.register_blueprint(value)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # debug=True gives helpful error pages while you're building the app,
    # but it's not safe to leave on if this app ever ran on a real server --
    # it would let anyone run code through the browser. This line checks
    # for a setting called FLASK_DEBUG. If it isn't set, debug stays off,
    # so you have to turn it on on purpose while coding, e.g. in the
    # terminal: (Windows) $env:FLASK_DEBUG="True"  or (Mac/Linux) export FLASK_DEBUG=True
    debug_mode = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    app.run(debug=debug_mode)
