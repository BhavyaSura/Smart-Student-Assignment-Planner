from flask_sqlalchemy import SQLAlchemy

# This is our connection to the database. We set it up once here,
# then connect it to the actual app inside app.py.
#
# Each feature adds its own class below this line for whatever it
# needs to save (a Course, an Assignment, a StudyGoal, etc). Adding a
# new class doesn't require changing anything above it, so two people
# adding classes at the same time is unlikely to cause conflicts --
# just try to add your class at the bottom, after everyone else's.
db = SQLAlchemy()
