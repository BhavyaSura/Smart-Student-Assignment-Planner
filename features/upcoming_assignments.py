from flask import Blueprint, render_template
from models import Assignment
upcoming_assignments_bp = Blueprint(
    'upcoming_assignments',
    __name__,
    url_prefix='/upcoming-assignments'
)
@upcoming_assignments_bp.route('/')
def upcoming_assignments():
    assignments = Assignment.query.filter(
        Assignment.due_date.isnot(None)
    ).order_by(
        Assignment.due_date.asc()
    ).all()
    return render_template(
        'assignments.html',
        assignments=assignments
    )