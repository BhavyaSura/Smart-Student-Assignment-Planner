from flask import Blueprint, render_template
from models import Assignment
progress_bp = Blueprint(
    'progress',
    __name__,
    url_prefix='/assignment-progress'
)
@progress_bp.route('/')
def assignment_progress():
    # Get all assignments from the database.
    assignments = Assignment.query.all()

    # Count assignments by status.
    total_assignments = len(assignments)

    not_started = sum(
        1 for assignment in assignments
        if assignment.status == 'Not Started'
    )

    in_progress = sum(
        1 for assignment in assignments
        if assignment.status == 'In Progress'
    )

    completed = sum(
        1 for assignment in assignments
        if assignment.status == 'Completed'
    )

    # Calculate overall completion percentage.
    if total_assignments > 0:
        completion_percentage = round(
            (completed / total_assignments) * 100
        )
    else:
        completion_percentage = 0

    return render_template(
        'progress.html',
        total_assignments=total_assignments,
        not_started=not_started,
        in_progress=in_progress,
        completed=completed,
        completion_percentage=completion_percentage
    )