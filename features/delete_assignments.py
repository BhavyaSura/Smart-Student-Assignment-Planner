from flask import (
    Blueprint, render_template, redirect, url_for, session
)
from models import db, Assignment


delete_assignments_bp = Blueprint('delete_assignments', __name__)


@delete_assignments_bp.route('/delete-assignments')
def delete_assignments():
    # Show only the signed-in student's assignments.
    assignments = Assignment.query.filter_by(
        user_id=session['user_id']
    ).all()

    return render_template(
        'delete_assignments.html',
        assignments=assignments
    )


@delete_assignments_bp.route(
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
        url_for('delete_assignments.delete_assignments')
    )