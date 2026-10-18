from datetime import date, timedelta
from flask import Blueprint, render_template, session
from models import db, Assignment

upcoming_assignments_bp = Blueprint(
    'upcoming_assignments',
    __name__,
    url_prefix='/upcoming-assignments'
)

@upcoming_assignments_bp.route('/')
def upcoming_assignments():
    today = date.today().isoformat()
    due_soon_limit = (date.today() + timedelta(days=3)).isoformat()

    # Get upcoming, incomplete assignments for the logged-in user.
    assignments = Assignment.query.filter_by(
        user_id=session['user_id']
    ).filter(
        db.or_(
            Assignment.due_date == None,
            Assignment.due_date == '',
            Assignment.due_date >= today
        ),
        Assignment.status != 'Completed'
    ).order_by(Assignment.due_date.asc()).all()

    # Assignments due today through the next 3 days.
    due_soon = [
        assignment for assignment in assignments
        if assignment.due_date
        and today <= assignment.due_date <= due_soon_limit
    ]

    return render_template(
        'assignments.html',
        assignments=assignments,
        due_soon=due_soon
    )