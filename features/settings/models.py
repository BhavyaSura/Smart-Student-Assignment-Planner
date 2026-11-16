"""
features/settings/models.py -- Student settings and preferences.
"""

from models import db


class UserSettings(db.Model):
    __tablename__ = 'user_settings'

    id = db.Column(db.Integer, primary_key=True)

    # Each student has their own settings.
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        unique=True,
        nullable=False
    )

    # Name displayed on the dashboard.
    display_name = db.Column(
        db.String(100),
        nullable=True
    )

    # Hide completed assignments.
    hide_completed = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    # Highlight assignments due within 1, 3, or 7 days.
    due_soon_days = db.Column(
        db.Integer,
        default=3,
        nullable=False
    )
