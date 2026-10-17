# How to add your own feature

If we all edit the same files, Git gets confused about whose changes
go where. To avoid that, **every feature gets its own folder** inside
`features`, and its own page templates inside `templates`. You will NOT
need to open or change `app.py` or `base.html` -- the app finds your
folder and draws your menu button by itself.

Each button in the left menu is the "home" of one feature:

| Menu button | Feature folder        | Template folder        |
|-------------|-----------------------|------------------------|
| Dashboard   | `features/dashboard/` | `templates/dashboard/` |
| Courses     | `features/courses/`   | `templates/courses/`   |
| Assignments | `features/assignments/` | `templates/assignments/` |
| Calendar    | `features/calendar/`  | `templates/calendar/`  |
| Progress    | `features/progress/`  | `templates/progress/`  |

(`features/auth/` has the sign-in pages. It has no menu button.)

Calendar (SSAP-19) and Progress (SSAP-9) start as empty pages with a dashed "coming
soon" box. To build one, open its folder and replace the dashed box --
the menu button already exists, so you do NOT need to create a new
folder or add a button.

The Dashboard is split into boxes. Each box has its own template file
in `templates/dashboard/` (like `suggested_summary_cards.html`) and its own small
Python file in `features/dashboard/` (like `suggested_summary_cards.py`). Replace
the dashed box in your template and fill in your Python file.

## Steps for a brand-new feature

1. Copy the `features/courses` folder and rename the copy to match your
   feature, like `features/grades`.

2. Open `features/grades/__init__.py`. Change the word "courses" (all
   places) to your feature's name:

   `grades_bp = Blueprint('grades', __name__)`

   This one line creates your feature's group of pages. Every page in
   your folder attaches to it.

3. Open `features/grades/routes.py`. Change the routes and the code
   inside them to do what your feature needs. A "route" is just a web
   page address, like `/grades`. Add more files if you want (like
   `details.py`); then add their names to the last line of
   `__init__.py`: `from . import routes, details`

4. Put your pages in `templates/grades/` and show them with
   `render_template('grades/home.html')`.

5. If your feature needs to save information (like a course, a task,
   a grade), make `features/grades/models.py` and write a class in it,
   the same way `Course` is written in the main `models.py`. Start the
   file with `from models import db`. Each class becomes its own table.
   Then add `from . import models` to the bottom of your `__init__.py`
   so the table gets created. (Using your own file means you never edit
   the shared `models.py`, so it can't conflict.)

6. Every page needs a signed-in student, and each student only sees
   their own data. So:
   - Give your model a `user_id` column, like `Course` has.
   - When you save something, include `user_id=session['user_id']`.
   - When you read something, filter by it:
     `Course.query.filter_by(user_id=session['user_id'])`
   (Remember to import `session` from flask.)

7. Add your menu button. In `features/grades/__init__.py`, edit the
   `NAV` block (it is already there if you copied a folder):

   ```
   NAV = {
       'label': 'Grades',               # words on the button
       'endpoint': 'grades.grades',     # blueprint name + page function name
       'order': 60,                     # position in the menu (small = higher)
       'icon': 'M...',                  # picture, as an SVG path
   }
   ```

   Orders now: Dashboard 10, Courses 20, Assignments 30, Calendar 40,
   Progress 50. The button stays highlighted on every page in your
   feature by itself. You do not edit `base.html`.

8. Run the app with `python app.py` and open your new page in the
   browser to make sure it works.

`app.py` finds your folder by itself, so it never needs to change.

## Rules that keep everything working

- Every feature folder needs an `__init__.py` file. Without it, your
  feature is not found.
- In `__init__.py`, the `from . import ...` line must stay BELOW the
  Blueprint line.
- Only ONE Blueprint per feature folder. Page files do
  `from . import grades_bp` and use it for their routes.

## A very small feature can be a single file

If your feature is one page, you can skip the folder: one file in
`features/` that creates its own Blueprint and routes also works.

## About the `suggested_` names

The folders and main files (`__init__.py`, `routes.py`, `base.html`, the
shared CSS files) are the basic structure, so they keep plain names.

The starter files we left for each person to fill in -- the dashboard
boxes -- start with `suggested_`. That just means "this is a suggested
name". You can rename them, and you can name your own new files
whatever you like. If you rename a file, update the line that uses it:

| If you rename... | Also update... |
|------------------|----------------|
| a dashboard Python file (`suggested_summary_cards.py`) | its `from .suggested_summary_cards import ...` line in `features/dashboard/routes.py` |
| a dashboard template (`suggested_summary_cards.html`) | its `{% include %}` line in `templates/dashboard/home.html` |
| a stylesheet | the `<link>` line that loads it |

Tip: search for the old name (Ctrl+Shift+F in VS Code), then run
`python app.py` and click through the pages to check everything works.

## Your own styles

Use the color names in `static/css/theme.css` (like `var(--accent)` and
`var(--border)`) so your pages match everyone else's. For extra styles,
make your own file (for example `static/css/suggested_grades.css`) and load it from
your template:

```
{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/suggested_grades.css') }}">
{% endblock %}
```

See `static/css/README.md` for what each shared file is for.
