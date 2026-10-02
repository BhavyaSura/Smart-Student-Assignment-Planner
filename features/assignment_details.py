from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Assignment
assignment_details_bp = Blueprint(
    'assignment_details',
    __name__,
    url_prefix='/assignment-details'
)
@assignment_details_bp.route('/<int:assignment_id>', methods=['GET', 'POST'])
def assignment_details(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    if request.method == 'POST':
        assignment.course = request.form['course'].strip()
        assignment.due_date = request.form['due_date']
        assignment.priority = request.form['priority']
        assignment.estimated_time = request.form['estimated_time'].strip()
        assignment.status = request.form['status']
        db.session.commit()
        return redirect(
            url_for(
                'upcoming_assignments.upcoming_assignments'
            )
        )
    return render_template(
        'assignment_details.html',
        assignment=assignment
    )