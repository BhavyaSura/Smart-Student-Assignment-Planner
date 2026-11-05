"""
features/courses/models.py -- Courses: the GradeItem table. (SSAP-30)

One row = one graded thing in a course, like "Midterm" or "Homework".
It lives in this feature's own file (not the shared models.py), so it
can't cause merge conflicts with anyone else.

New table only -- nothing about the existing tables changes. When the
app starts, db.create_all() in app.py adds this table to planner.db
by itself.
"""
from models import db


class GradeItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Who owns it, and which course it belongs to.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    # This lets us write course.grade_items to get a course's items.
    course = db.relationship('Course', backref='grade_items')

    name = db.Column(db.String(100), nullable=False)    # e.g. "Midterm"
    weight = db.Column(db.Float, nullable=False)        # % of the final grade, e.g. 25
    score = db.Column(db.Float, nullable=True)          # % earned, e.g. 88. Empty = not graded yet

    def __repr__(self):
        return f'<GradeItem {self.name}>'
