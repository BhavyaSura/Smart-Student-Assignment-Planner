"""
features/assignments/upcoming.py -- Assignments: the "Upcoming Assignments" list. This is the home page
of the Assignments feature.
"""
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from flask import render_template, session
from models import db, Assignment
from . import assignments_bp
from features.settings.models import UserSettings

@assignments_bp.route('/upcoming-assignments/')
def upcoming_assignments():
    # Use Eastern time, not the server's clock (PythonAnywhere uses UTC).
    today_date = datetime.now(ZoneInfo("America/New_York")).date()
    today = today_date.isoformat()  # e.g. "2026-10-02"

    # "Upcoming" = due today or later, OR no due date recorded yet
    # (so a brand-new assignment doesn't vanish before its details
    # are filled in), AND not already marked Completed.
    # Get the signed-in student's preference.
    user_settings = UserSettings.query.filter_by(
        user_id=session['user_id']
    ).first()

    # Hide completed assignments by default.
    hide_completed = (
        user_settings.hide_completed
        if user_settings else True
    )

    # Keep the existing due-date filtering.
    query = Assignment.query.filter_by(
        user_id=session['user_id']
    ).filter(
        db.or_(
            Assignment.due_date == None,
            Assignment.due_date == '',
            Assignment.due_date >= today
        )
    )

    # Apply the student's preference.
    if hide_completed:
        query = query.filter(Assignment.status != 'Completed')

    assignments = query.order_by(Assignment.due_date.asc()).all()

    # Use the student's selected Due Soon reminder window.
    reminder_days = (
        user_settings.due_soon_days
        if user_settings and user_settings.due_soon_days in (1, 3, 7)
        else 3
    )

    due_soon_limit = (
        today_date + timedelta(days=reminder_days)
    ).isoformat()
    due_soon = [
        assignment for assignment in assignments
        if assignment.due_date
        and today <= assignment.due_date <= due_soon_limit
        # Completed work never needs a reminder, even when
        # "Hide Completed Assignments" is turned off.
        and assignment.status != 'Completed'
    ]

    return render_template(
        'assignments/upcoming.html',
        assignments=assignments,
        due_soon=due_soon
    )
