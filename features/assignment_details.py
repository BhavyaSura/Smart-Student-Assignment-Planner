from flask import Blueprint, render_template, request, redirect, url_for, session
from models import db, Assignment, Course

assignment_details_bp = Blueprint(
    'assignment_details',
    __name__,
    url_prefix='/assignment-details'
)


@assignment_details_bp.route('/<int:assignment_id>', methods=['GET', 'POST'])
def assignment_details(assignment_id):

    assignment = Assignment.query.filter_by(
        id=assignment_id,
        user_id=session['user_id']
    ).first_or_404()

    courses = Course.query.filter_by(
        user_id=session['user_id']
    ).all()

    if request.method == 'POST':

        title = request.form.get('title', '').strip()
        course_id = request.form.get('course_id', '').strip()
        due_date = request.form.get('due_date', '').strip()
        priority = request.form.get('priority', '').strip()
        estimated_time = request.form.get('estimated_time', '').strip()
        status = request.form.get('status', '').strip()

        if not (
            title
            and course_id
            and due_date
            and priority
            and estimated_time
            and status
        ):
            return render_template(
                'assignment_details.html',
                assignment=assignment,
                courses=courses,
                error='Please fill out every field.'
            )

        course = Course.query.filter_by(
            id=course_id,
            user_id=session['user_id']
        ).first()

        if course is None:
            return render_template(
                'assignment_details.html',
                assignment=assignment,
                courses=courses,
                error='Please choose a valid course.'
            )

        assignment.title = title
        assignment.course = course
        assignment.due_date = due_date
        assignment.priority = priority
        assignment.estimated_time = estimated_time
        assignment.status = status

        db.session.commit()

        return redirect(
            url_for('upcoming_assignments.upcoming_assignments')
        )

    return render_template(
        'assignment_details.html',
        assignment=assignment,
        courses=courses
    )