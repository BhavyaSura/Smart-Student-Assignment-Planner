"""
features/progress/routes.py -- Progress: the Assignment Progress Overview page.
It counts the signed-in student's assignments by status and works out
the overall completion percentage. (SSAP-9, built by Bhavya.)
"""
from flask import render_template, session
from models import Assignment
from . import progress_bp


@progress_bp.route('/')
def assignment_progress():
    # Get all of this student's assignments from the database.
    assignments = Assignment.query.filter_by(
        user_id=session['user_id']
    ).all()

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
        'progress/home.html',
        total_assignments=total_assignments,
        not_started=not_started,
        in_progress=in_progress,
        completed=completed,
        completion_percentage=completion_percentage
    )
