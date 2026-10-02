from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# SSAP-5 - Course Feature
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20))
    instructor = db.Column(db.String(100))
    def __repr__(self):
        return f'<Course {self.name}>'
# Assignment Feature
class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Used by the Add Assignment feature
    title = db.Column(db.String(200), nullable=False)
    # Assignment details
    course = db.Column(db.String(100), nullable=True)
    due_date = db.Column(db.String(20), nullable=True)
    priority = db.Column(db.String(20), nullable=True)
    estimated_time = db.Column(db.String(50), nullable=True)
    # Assignment status
    status = db.Column(
        db.String(30),
        nullable=False,
        default="Not Started"
    )