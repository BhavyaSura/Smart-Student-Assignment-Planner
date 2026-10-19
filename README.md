# Smart Student Assignment Planner

Flask app for planning courses and assignments, based on the Flask Todo App structure reviewed by the team.

## Features implemented so far
- Create an account, sign in, and sign out (SSAP-16, SSAP-15)
- Add and view courses (SSAP-5)
- Add a new assignment (SSAP-2)
- View upcoming assignments (due today or later, not completed)
- Edit assignment details: title, course, due date, priority, time, status
- Delete assignments
- Each student only sees their own courses and assignments

## How the code is organized

Every feature has its own folder, and each button in the left menu is
the home page of one feature:

```
features/
  dashboard/     Dashboard (boxes for features still being built)
  courses/       Courses (an "Add a course" square plus one square per course)
  assignments/   Assignments (upcoming, add, edit, delete)
  calendar/      Calendar (empty for now)
  progress/      Progress overview (counts by status and a completion bar)
  auth/          Create account, sign in, sign out
templates/
  base.html      the page frame (the side menu is built from each feature's NAV)
  one folder per feature, with that feature's pages
static/css/
  theme.css      colors and fonts (change a color here to restyle the app)
  layout.css     sidebar and page frame
  components.css forms, buttons, the dashed "coming soon" box
  dashboard.css  styles only the Dashboard uses
  courses.css    styles only the Courses page uses
  progress.css   styles only the Progress page uses
models.py        shared database tables
app.py           starts the app and turns on every feature by itself
```

Each folder has a short README that says what its files are for.

Files that start with `suggested_` (the dashboard boxes) are starter files
with a *suggested* name. Teammates can rename them freely; see
HOW_TO_ADD_A_FEATURE.md.

New features go in their own folder inside `features/` -- see
HOW_TO_ADD_A_FEATURE.md for how to add one.

## Run locally

1. Create a virtual environment: `python -m venv .venv`
2. Activate it:
   - Windows: `.venv\Scripts\Activate.ps1`
   - Mac/Linux: `source .venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python app.py`
5. Open http://127.0.0.1:5000/

The app creates a new `planner.db` automatically the first time you run
`python app.py`. If you already have an old `planner.db` from before the
account update, delete it first, or you will get a "no such column" error:
- Windows: `Remove-Item instance\planner.db`
- Mac/Linux: `rm instance/planner.db`

Sign-in uses a secret key to protect the login cookie. For local testing
the app has a built-in fallback, so you don't need to set anything. To use
your own, set the `SECRET_KEY` environment variable.

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
