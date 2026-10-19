"""
features/assignments/upcoming.py -- Assignments: the "Upcoming Assignments" list. This is the home page
of the Assignments feature.
"""
from datetime import date, timedelta
from flask import render_template, session
from models import db, Assignment
from . import assignments_bp


@assignments_bp.route('/upcoming-assignments/')
def upcoming_assignments():
    today = date.today().isoformat()  # e.g. "2026-10-02"

    # "Upcoming" = due today or later, OR no due date recorded yet
    # (so a brand-new assignment doesn't vanish before its details
    # are filled in), AND not already marked Completed.
    assignments = Assignment.query.filter_by(user_id=session['user_id']).filter(
        db.or_(
            Assignment.due_date == None,
            Assignment.due_date == '',
            Assignment.due_date >= today
        ),
        Assignment.status != 'Completed'
    ).order_by(Assignment.due_date.asc()).all()

    # SSAP-13: assignments due today through the next 3 days.
    due_soon_limit = (date.today() + timedelta(days=3)).isoformat()
    due_soon = [
        assignment for assignment in assignments
        if assignment.due_date
        and today <= assignment.due_date <= due_soon_limit
    ]

    return render_template(
        'assignments/upcoming.html',
        assignments=assignments,
        due_soon=due_soon
    )
