# Smart Student Assignment Planner

Minimal Flask starter based on the Flask Todo App structure reviewed by the team. This starter provides only a home page and SQLAlchemy initialization. No planner backlog feature is implemented yet.

## Run locally

1. Create a virtual environment: `python -m venv .venv`
2. Activate it:
   - Windows: `.venv\Scripts\Activate.ps1`
   - Mac/Linux: `source .venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python app.py`
5. Open http://127.0.0.1:5000/

By default the app runs with debug mode off, which is the safer
setting. While you're actively coding and want to see detailed error
pages, turn it on for that terminal session only:
- Windows: `$env:FLASK_DEBUG="True"`
- Mac/Linux: `export FLASK_DEBUG=True`

## Upstream Source and License

This project uses the Flask Todo App by GPannu77 as its starting point.
Original repository: https://github.com/GPannu77/Flask-Todo-App
We reused and adapted the basic Flask application structure,
SQLAlchemy initialization, HTML templates, and CSS layout.
The original task-management features were removed from our starter
version so our team can develop the Smart Student Assignment Planner
features through our Jira backlog.
The original project's MIT license notice is preserved in the
LICENCE file.
