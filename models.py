from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# SSAP-5 - Course Feature
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,
                         db.ForeignKey('user.id'),
                         nullable=False)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20))
    instructor = db.Column(db.String(100))
    def __repr__(self):
        return f'<Course {self.name}>'
# Assignment Feature
class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,
                         db.ForeignKey('user.id'),
                         nullable=False)
    # Used by the Add Assignment feature
    title = db.Column(db.String(200), nullable=False)
    # Assignment details
    # This links an assignment to a real Course row by its ID, instead
    # of just copying the course's name as plain text. If a course
    # gets renamed, every assignment linked to it shows the new name
    # automatically, because they all point to the same row.
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=True)
    course = db.relationship('Course', backref='assignments')
    due_date = db.Column(db.String(20), nullable=True)
    priority = db.Column(db.String(20), nullable=True)
    estimated_time = db.Column(db.String(50), nullable=True)
    # Assignment status
    status = db.Column(
        db.String(30),
        nullable=False,
        default="Not Started"
    )

# SSAP-16 / SSAP-15 - Account Feature
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # unique=True means two accounts can't use the same email.
    email = db.Column(db.String(120), unique=True, nullable=False)
    # We never save the real password -- only a scrambled version
    # (a "hash") that can't be turned back into the original.
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'
