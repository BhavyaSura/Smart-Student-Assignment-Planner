"""
features/dashboard/due_soon_alert.py -- Dashboard Due Soon alerts.

Uses each student's preferred reminder window (1, 3, or 7 days).
Only includes incomplete assignments.
"""

from datetime import date, timedelta
from models import Assignment
from features.settings.models import UserSettings


def due_soon_alert(user_id):
    # Get this student's reminder preference.
    user_settings = UserSettings.query.filter_by(
        user_id=user_id
    ).first()

    # Default to 3 days if no preference is saved.
    reminder_days = (
        user_settings.due_soon_days
        if user_settings and user_settings.due_soon_days in (1, 3, 7)
        else 3
    )

    today = date.today().isoformat()
    due_soon_limit = (
        date.today() + timedelta(days=reminder_days)
    ).isoformat()

    return Assignment.query.filter_by(
        user_id=user_id
    ).filter(
        Assignment.due_date >= today,
        Assignment.due_date <= due_soon_limit,
        Assignment.status != 'Completed'
    ).order_by(Assignment.due_date.asc()).all()
