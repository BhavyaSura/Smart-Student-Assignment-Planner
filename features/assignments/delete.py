"""
features/assignments/delete.py -- Assignments: the page that lists assignments and deletes the one
the student picks.
"""
from flask import render_template, redirect, url_for, session
from models import db, Assignment
from . import assignments_bp


@assignments_bp.route('/delete-assignments')
def delete_assignments():
    # Show only the signed-in student's assignments.
    assignments = Assignment.query.filter_by(
        user_id=session['user_id']
    ).all()

    return render_template(
        'assignments/delete.html',
        assignments=assignments
    )


@assignments_bp.route(
    '/delete-assignment/<int:assignment_id>',
    methods=['POST']
)
def delete_assignment(assignment_id):
    # Only allow the student to delete their own assignment.
    assignment = Assignment.query.filter_by(
        id=assignment_id,
        user_id=session['user_id']
    ).first_or_404()

    db.session.delete(assignment)
    db.session.commit()

    return redirect(
        url_for('assignments.delete_assignments')
    )