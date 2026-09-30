from flask import Blueprint, render_template, redirect, url_for
from models import db, Assignment


delete_assignments_bp = Blueprint('delete_assignments', __name__)


@delete_assignments_bp.route('/delete-assignments')
def delete_assignments():
    assignments = Assignment.query.all()

    return render_template(
        'delete_assignments.html',
        assignments=assignments
    )


@delete_assignments_bp.route(
    '/delete-assignment/<int:assignment_id>',
    methods=['POST']
)
def delete_assignment(assignment_id):
    assignment = db.session.get(Assignment, assignment_id)

    if assignment:
        db.session.delete(assignment)
        db.session.commit()

    return redirect(
        url_for('delete_assignments.delete_assignments')
    )