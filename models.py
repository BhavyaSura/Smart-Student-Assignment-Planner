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
class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    due_date = db.Column(db.String(20), nullable=False)
    priority = db.Column(db.String(20), nullable=False)
    estimated_time = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(30), nullable=False, default="Not Started")

# SSAP-5 - Course Feature
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20))
    instructor = db.Column(db.String(100))

    def __repr__(self):
        return f'<Course {self.name}>'