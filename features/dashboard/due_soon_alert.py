"""
features/dashboard/due_soon_alert.py -- the data for the "Due Soon" box on
the Dashboard (SSAP-13, built by Bhavya).

It finds this student's assignments that are due from today up to 3 days
from now and are not completed yet. The box is drawn by
templates/shared/due_soon_alert.html
"""
from datetime import date, timedelta
from models import Assignment


def due_soon_alert(user_id):
    today = date.today().isoformat()
    due_soon_limit = (date.today() + timedelta(days=3)).isoformat()

    return Assignment.query.filter_by(
        user_id=user_id
    ).filter(
        Assignment.due_date >= today,
        Assignment.due_date <= due_soon_limit,
        Assignment.status != 'Completed'
    ).order_by(Assignment.due_date.asc()).all()
