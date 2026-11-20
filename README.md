# Smart Student Assignment Planner (SSAP)

Smart Student Assignment Planner is a web app built with Python and Flask that helps
college students keep track of their courses, assignments, deadlines, and grades in
one place. Each student signs in to their own private planner, sees what's due this
week at a glance, and can work out what grade they need to reach their goal in a
course.

**Live site:** https://miczi55.pythonanywhere.com

## Features

### Accounts
- **Create an Account**: Sign up with an email and a password (at least 8 characters).
- **Sign In and Sign Out**: Each student only ever sees their own courses, assignments, and grades.

### Dashboard
- **Greeting**: Shows today's date, a "good morning / afternoon / evening" greeting, and a red alert when something is overdue.
- **Summary Cards**: Total, completed, due this week, and overdue assignments at a glance.
- **Course Cards**: A card for each course with its completion progress.
- **This Week**: Everything due in the next 7 days, with "Tomorrow", "Saturday", and other easy-to-read dates.
- **Mini Calendar**: The current month, with a blue dot for work due and a green dot for completed work.
- **Upcoming**: Work due after this week, plus assignments with no due date.
- **Due Soon Alert**: A reminder box for anything due in the next few days (the number of days is set in Settings).

### Courses
- **Add a Course**: Save a course's name, code, and instructor.
- **Course Page**: See the course's progress and every assignment for that course.
- **Grade Tracking**: Add, edit, and delete grade items (like "Midterm, 25%, scored 84").
- **Grade Calculator**: Pick a goal (like "To get: 90%") and see what score you need on the rest of the course.
- **Delete a Course**: Removes the course along with its assignments and grades (asks first).

### Assignments
- **Add an Assignment**: Title, course, due date, priority, estimated time, and status.
- **Edit an Assignment**: Change any detail, including marking it In Progress or Completed.
- **Upcoming Assignments**: Every upcoming assignment in one list, with friendly dates and color-coded status badges.
- **Delete Assignments**: Remove assignments you no longer need.

### Calendar
- **Monthly Calendar**: See every assignment on the day it's due, color-coded by status.
- **Filters**: Show only one course and/or one status.
- **Day Details**: Click a day to see what's due.
- **Today Button**: Jump back to the current month.

### Progress
- **Progress Overview**: Counts of Not Started, In Progress, and Completed assignments.
- **Overall Completion**: A percentage and progress bar for all of your work.

### Settings
- **Display Name**: Choose the name shown in your greeting.
- **Hide Completed Assignments**: Keep finished work out of the Upcoming list.
- **Due Soon Reminder**: Choose 1, 3, or 7 days ahead.
- **Reset Data**: Delete all of your courses, assignments, and grades (you must type `RESET`).

### Appearance
- **Dark Mode**: Switch between light and dark from the sidebar or Settings.
- **Planner Color**: Pick your own background color.
- **Phone Friendly**: The layout adjusts to small screens.

## Getting Started

> SSAP runs on **Windows, Mac, and Linux**. You need **Python 3.10 or newer**
> and **Git**.

### Use the Live Site

1. **Open the site**:
   - Go to https://miczi55.pythonanywhere.com      

2. **Create an account**:
   - Click **Create one**, enter an email and a password, then sign in.

> The live site is a class project, so its data is test data and may be reset.

### Run It on Your Own Computer

> **Note**: Check your Python version first with `python --version` (Windows)
> or `python3 --version` (Mac/Linux). If it's missing or older than 3.10,
> download it from https://www.python.org/downloads/. On Windows, check
> **"Add python.exe to PATH"** on the first install screen.

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BhavyaSura/Smart-Student-Assignment-Planner.git
   ```
   This downloads the project to your computer.

2. **Move Into the Folder**:
   ```bash
   cd Smart-Student-Assignment-Planner
   ```
   This moves your terminal into the project folder.

3. **Create a Virtual Environment** (first time only):
   - Windows:
     ```bash
     python -m venv .venv
     ```
   - Mac/Linux:
     ```bash
     python3 -m venv .venv
     ```
   This makes a private `.venv` folder of packages just for this project.

4. **Activate the Virtual Environment** (every time you open a new terminal):
   - Windows (PowerShell):
     ```bash
     .venv\Scripts\Activate.ps1
     ```
   - Mac/Linux:
     ```bash
     source .venv/bin/activate
     ```
   Your terminal line should now start with `(.venv)`.

   > **Windows error "running scripts is disabled on this system"?** Run
   > `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then try again.

5. **Install the Packages** (first time, and whenever `requirements.txt` changes):
   ```bash
   pip install -r requirements.txt
   ```
   This installs Flask, Flask-SQLAlchemy, Flask-WTF, and tzdata (time zone data).

6. **Run the App**:
   ```bash
   python app.py
   ```
   This starts the app on your computer.

7. **Open It in Your Browser**:
   - Go to http://127.0.0.1:5000 and create an account.
   - Press **Ctrl+C** in the terminal to stop the app.

### Every Time You Come Back

```bash
cd Smart-Student-Assignment-Planner
git pull
```
`git pull` downloads your teammates' latest changes. Then activate the virtual
environment (step 4), run `pip install -r requirements.txt` if it changed, and
start the app with `python app.py`.

### Your Local Database

The app creates `instance/planner.db` the first time it runs. It's in
`.gitignore`, so your local data is never pushed to GitHub, and it's separate
from the live site's data.

If you see a **"no such column"** error after `git pull`, someone changed a
database table. Delete your local database and run the app again:
- Windows: `Remove-Item instance\planner.db`
- Mac/Linux: `rm instance/planner.db`

### Optional: Debug Mode

Debug mode shows detailed error pages while you code. It's off by default.
Turn it on for one terminal session before running `python app.py`:
- Windows (PowerShell): `$env:FLASK_DEBUG="True"`
- Mac/Linux: `export FLASK_DEBUG=True`

## How the Code Is Organized

Every feature has its own folder, and each button in the left menu is the home
page of one feature. That way teammates can work on different features without
editing the same files.

```
app.py              starts the app and turns on every feature automatically
models.py           shared database tables (User, Course, Assignment)
requirements.txt    packages to install
features/
  auth/             create account, sign in, sign out
  dashboard/        the Dashboard and each of its boxes
  courses/          courses, course pages, grade tracking, grade calculator
  assignments/      add, edit, delete, and the Upcoming Assignments list
  calendar/         the monthly calendar and its filters
  progress/         the Progress overview
  settings/         the Settings page and Reset Data
templates/
  base.html         the page frame and sidebar
  one folder per feature, with that feature's pages
static/
  css/theme.css     all colors for light and dark mode
  css/layout.css    the sidebar and page frame
  css/components.css shared forms and buttons
  css/<feature>.css styles used by only one page
  js/               small scripts (the calendar's day popup)
```

To add a new feature, see [HOW_TO_ADD_A_FEATURE.md](HOW_TO_ADD_A_FEATURE.md).

### When You Change the Database

If your change adds, renames, or removes a column in an existing table, **say so
in your commit message** (for example: `added priority column to Assignment`).
Everyone then deletes their local `instance/planner.db`, and whoever deploys
deletes the live one. Adding a brand-new table does **not** need a reset; the app
creates new tables automatically.

## Hosting (PythonAnywhere)

The live site runs on a free PythonAnywhere account. Pushing to GitHub does
**not** update the live site by itself; whoever has the PythonAnywhere login
deploys updates.

### How It's Set Up

- The repo is cloned to `/home/Miczi55/Smart-Student-Assignment-Planner`.
- The web app uses **Manual configuration** with **Python 3.12**.
- The WSGI file (Web tab → *WSGI configuration file*) sets the `SECRET_KEY` and
  loads the app with `from app import app as application`. The secret key lives
  only on PythonAnywhere and is **never** put in this repo.

### Deploying New Code

1. **Open a Bash console** on PythonAnywhere (Consoles tab).
2. **Pull the new code**:
   ```bash
   cd ~/Smart-Student-Assignment-Planner
   git pull
   ```
3. **If `requirements.txt` changed**, install the new packages:
   ```bash
   pip3.12 install --user -r requirements.txt
   ```
4. **If an existing database table changed**, delete the live database (this
   erases all live accounts and data):
   ```bash
   rm instance/planner.db
   ```
5. **Reload**: go to the **Web** tab and click the green **Reload** button.

### Keeping the Site Online

The free plan turns the site off after one month. Every few weeks, go to the
**Web** tab and click **"Run until 1 month from today."**

### Something Broke?

Go to the **Web** tab → **Log files** → open the **error log** and read the last
few lines.

## Upstream Source and License

This project started from the [Flask Todo App](https://github.com/GPannu77/Flask-Todo-App)
by GPannu77. We reused and adapted its basic Flask structure, SQLAlchemy setup,
HTML templates, and CSS layout, then removed the original to-do features and built
the Smart Student Assignment Planner features through our Jira backlog. The original
project's MIT license notice is kept in the [LICENCE](LICENCE) file.
