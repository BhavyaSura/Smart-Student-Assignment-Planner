"""
features/assignments/add.py -- Assignments: the "Add new assignment" page (form + saving).
"""
# Miczi SSAP-2 add_new_assignments
#
# Coming from a course page (/add-assignment?course_id=3) turns this into
# a 2-step guide:
#   Step 1 (this page): name the assignment. It's saved to that course.
#   Step 2: the new assignment's edit page opens to fill in the rest.
#           Saving there takes you back to the course page.
from flask import render_template, request, redirect, url_for, session
from models import db, Assignment, Course
from . import assignments_bp


def course_from_request():
    # The course id comes from the address (?course_id=3) the first time,
    # and from a hidden box in the form when it's submitted.
    course_id = request.values.get('course_id', type=int)
    if course_id is None:
        return None

    # Only use it if it's one of the signed-in student's OWN courses.
    return Course.query.filter_by(
        id=course_id,
        user_id=session['user_id']
    ).first()


@assignments_bp.route('/add-assignment', methods=['GET', 'POST'])
def add_assignment():
    # None when you opened this page from the Assignments tab.
    course = course_from_request()

    if request.method == 'POST':
        title = request.form.get('title', '').strip()

        if not title:
            return render_template(
                'assignments/add.html',
                course=course,
                error='Please enter an assignment name.'
            )

        assignment = Assignment(title=title, user_id=session['user_id'])
        if course:
            assignment.course = course
        db.session.add(assignment)
        db.session.commit()

        if course:
            # Step 2: open the new assignment's edit page. from_course tells
            # it to come back to this course page after saving.
            return redirect(url_for(
                'assignments.assignment_details',
                assignment_id=assignment.id,
                from_course=course.id
            ))

        # Send them to the list so they can actually see what they added.
        return redirect(url_for('assignments.upcoming_assignments'))

    return render_template('assignments/add.html', course=course)
