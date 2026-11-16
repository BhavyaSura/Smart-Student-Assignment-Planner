"""
features/assignments/details.py -- Assignments: the page that shows and edits ONE assignment.
"""
from flask import render_template, request, redirect, url_for, session
from models import db, Assignment, Course
from . import assignments_bp


@assignments_bp.route(
    '/assignment-details/<int:assignment_id>',
    methods=['GET', 'POST']
)
def assignment_details(assignment_id):

    assignment = Assignment.query.filter_by(
        id=assignment_id,
        user_id=session['user_id']
    ).first_or_404()

    courses = Course.query.filter_by(
        user_id=session['user_id']
    ).all()

    # Step 2 of adding from a course page: the address has ?from_course=3.
    # We look the course up (only the student's own) so we can send them
    # back to it after saving. None means "go to the assignments list".
    back_course = None
    from_course = request.args.get('from_course', type=int)
    if from_course is not None:
        back_course = Course.query.filter_by(
            id=from_course,
            user_id=session['user_id']
        ).first()

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
                'assignments/details.html',
                assignment=assignment,
                courses=courses,
                back_course=back_course,
                error='Please fill out every field.'
            )

        course = Course.query.filter_by(
            id=course_id,
            user_id=session['user_id']
        ).first()

        if course is None:
            return render_template(
                'assignments/details.html',
                assignment=assignment,
                courses=courses,
                back_course=back_course,
                error='Please choose a valid course.'
            )

        assignment.title = title
        assignment.course = course
        assignment.due_date = due_date
        assignment.priority = priority
        assignment.estimated_time = estimated_time
        assignment.status = status

        db.session.commit()

        # Came from a course page? Go back there. Otherwise, the list.
        if back_course:
            return redirect(
                url_for('courses.course_details', course_id=back_course.id)
            )

        return redirect(
            url_for('assignments.upcoming_assignments')
        )

    return render_template(
        'assignments/details.html',
        assignment=assignment,
        courses=courses,
        back_course=back_course
    )