from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Assignment, Course

assignment_details_bp = Blueprint(
    'assignment_details',
    __name__,
    url_prefix='/assignment-details'
)


@assignment_details_bp.route('/<int:assignment_id>', methods=['GET', 'POST'])
def assignment_details(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    # List of existing courses, so the student picks one instead of
    # typing a course name that might not match anything in Courses.
    courses = Course.query.all()

    if request.method == 'POST':
        course_id = request.form.get('course_id', '').strip()
        due_date = request.form.get('due_date', '').strip()
        priority = request.form.get('priority', '').strip()
        estimated_time = request.form.get('estimated_time', '').strip()
        status = request.form.get('status', '').strip()

        if not (course_id and due_date and priority and estimated_time and status):
            return render_template(
                'assignment_details.html',
                assignment=assignment,
                courses=courses,
                error='Please fill out every field.'
            )

        # Look up the actual Course row by its ID, so the assignment
        # links to it directly instead of copying its name as text.
        course = Course.query.get(course_id)
        if course is None:
            return render_template(
                'assignment_details.html',
                assignment=assignment,
                courses=courses,
                error='Please choose a valid course.'
            )

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
