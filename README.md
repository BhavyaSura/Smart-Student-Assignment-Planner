# Smart Student Assignment Planner

Flask app for planning courses and assignments, based on the Flask Todo App structure reviewed by the team.

**Live site:** https://jiovanyo.pythonanywhere.com

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

---

## Running the app

There are two ways to use the app:

| | Where it runs | Who uses it |
|---|---|---|
| **Locally** | Your own computer, at http://127.0.0.1:5000 | You, while coding and testing |
| **Hosted** | PythonAnywhere, at https://jiovanyo.pythonanywhere.com | Anyone with the link |

Each one has its **own separate database**. Accounts you make locally
don't exist on the live site, and the other way around.

---

## Part 1: Run locally (for development)

### Step 1: Install Python (one time only)

You need Python 3.10 or newer.

1. Check if you already have it:
   - Windows: `python --version`
   - Mac/Linux: `python3 --version`
2. If you get an error or a version older than 3.10, download it from
   https://www.python.org/downloads/
   - **Windows:** on the first install screen, check the box
     **"Add python.exe to PATH"** before clicking Install.
3. Close and reopen your terminal, then run the version check again.

### Step 2: Get the code (one time only)

```bash
git clone https://github.com/BhavyaSura/Smart-Student-Assignment-Planner.git
cd Smart-Student-Assignment-Planner
```

The first command downloads the project, and the second moves into its folder.

### Step 3: Create a virtual environment (one time only)

A virtual environment (`.venv`) is a private folder of Python packages just
for this project, so it doesn't mess with anything else on your computer.

- Windows: `python -m venv .venv`
- Mac/Linux: `python3 -m venv .venv`

This creates the `.venv` folder inside the project. It's already in
`.gitignore`, so it never gets pushed to GitHub.

### Step 4: Activate the virtual environment (every time you open a new terminal)

- Windows (PowerShell): `.venv\Scripts\Activate.ps1`
- Mac/Linux: `source .venv/bin/activate`

You'll know it worked when your terminal line starts with `(.venv)`.

> **Windows error "running scripts is disabled on this system"?** Run this
> once, then try activating again:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

### Step 5: Install the packages (first time, and whenever requirements.txt changes)

```bash
pip install -r requirements.txt
```

This installs Flask and Flask-SQLAlchemy into your virtual environment.

### Step 6: Run the app

```bash
python app.py
```

Then open http://127.0.0.1:5000/ in your browser. Press **Ctrl+C** in the
terminal to stop the server.

### Your local database

The app creates `instance/planner.db` automatically the first time you run it.
The `instance/` folder is in `.gitignore`, so your local data is never pushed.

If you get a **"no such column"** error after pulling new code, someone changed
a database table. Delete your local database and run the app again:
- Windows: `Remove-Item instance\planner.db`
- Mac/Linux: `rm instance/planner.db`

### Secret key and debug mode (local)

Sign-in uses a secret key to protect the login cookie. For local testing
the app has a built-in fallback, so you don't need to set anything.

Debug mode is off by default, which is the safer setting. While you're
actively coding and want detailed error pages, turn it on for that terminal
session only:
- Windows: `$env:FLASK_DEBUG="True"`
- Mac/Linux: `export FLASK_DEBUG=True`

### Quick checklist for every coding session

```bash
cd Smart-Student-Assignment-Planner
git pull
# activate: .venv\Scripts\Activate.ps1  (Windows)  or  source .venv/bin/activate  (Mac/Linux)
python app.py
```

---

## Part 2: Hosted site (PythonAnywhere)

The live app runs on a free PythonAnywhere account at
**https://jiovanyo.pythonanywhere.com**. Only the person with that
PythonAnywhere login can deploy updates. Pushing to GitHub does **not**
update the live site by itself.

### How it's set up (for reference)

- The repo is cloned to `/home/jiovanyo/Smart-Student-Assignment-Planner`.
- Packages were installed with `pip3.12 install --user -r requirements.txt`.
- The web app uses **Manual configuration** with **Python 3.12**.
- The WSGI file (Web tab → *WSGI configuration file*) points to the project
  folder, sets the `SECRET_KEY`, and loads the app with
  `from app import app as application`. The secret key lives only on
  PythonAnywhere and is **not** in this repo.
- The live database is at `instance/planner.db` on PythonAnywhere.

### Deploying new code to the live site

1. Push your changes to GitHub like normal.
2. Log in to pythonanywhere.com and open a **Bash console** (Consoles tab).
3. Pull the new code:

   ```bash
   cd ~/Smart-Student-Assignment-Planner
   git pull
   ```

4. **If anyone changed an existing database table** (added, renamed, or
   removed a column), also delete the live database:

   ```bash
   rm instance/planner.db
   ```

   The app rebuilds it with the new structure. ⚠️ All accounts and data on
   the live site are erased, so make a new test account after.

5. **If `requirements.txt` changed**, install the new packages:

   ```bash
   pip3.12 install --user -r requirements.txt
   ```

6. Go to the **Web** tab and click the green **Reload** button.

> Not sure if the database changed? Run the `rm` command anyway. The live
> site only has test data.

### Keeping the site online

The free plan turns the site off after 1 month. Every few weeks, go to the
**Web** tab and click **"Run until 1 month from today."** It's free.

### Something broke on the live site?

Web tab → **Log files** → open the **error log** and read the last few lines.

---

## When you change the database

If your feature adds, renames, or removes columns in an existing model,
**say so in your commit message** (example: `added priority column to Assignment`).
That tells everyone to delete their local `instance/planner.db`, and tells
whoever deploys to delete the live one.

Adding a brand-new model (a new table) does **not** need a reset. The app
creates new tables automatically.

---

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
