from datetime import date
from flask import Blueprint, render_template, session
from models import db, Assignment

upcoming_assignments_bp = Blueprint(
    'upcoming_assignments',
    __name__,
    url_prefix='/upcoming-assignments'
)


@upcoming_assignments_bp.route('/')
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

    return render_template(
        'assignments.html',
        assignments=assignments
    )
