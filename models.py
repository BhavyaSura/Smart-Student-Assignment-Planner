from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(200), nullable=False)

    course = db.Column(db.String(100), nullable=False)

    due_date = db.Column(db.String(20), nullable=False)

    priority = db.Column(db.String(20), nullable=False)

    estimated_time = db.Column(db.String(50), nullable=False)

    status = db.Column(
        db.String(30),
        nullable=False,
        default="Not Started"
    )