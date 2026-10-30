"""
features/courses/delete.py -- Courses: deleting a course.

Two steps, so nobody deletes a course by accident:
  1. GET  /courses/<id>/delete  shows a "Are you sure?" page.
  2. POST /courses/<id>/delete  really deletes it (the button on that page).
"""
from flask import render_template, redirect, url_for, session
from models import db, Course
from . import courses_bp


@courses_bp.route('/courses/<int:course_id>/delete')
def confirm_delete_course(course_id):
    # Only find the course if it belongs to the signed-in student.
    course = Course.query.filter_by(
        id=course_id,
        user_id=session['user_id']
    ).first_or_404()

    # Show the "Are you sure?" page. It tells the student how many
    # assignments will be deleted with the course.
    return render_template('courses/delete.html', course=course)


@courses_bp.route('/courses/<int:course_id>/delete', methods=['POST'])
def delete_course(course_id):
    # Same check: a student can only delete their OWN course.
    course = Course.query.filter_by(
        id=course_id,
        user_id=session['user_id']
    ).first_or_404()

    # Delete the course's assignments first, so none are left behind
    # pointing at a course that no longer exists.
    for assignment in course.assignments:
        db.session.delete(assignment)

    db.session.delete(course)
    db.session.commit()

    # Go back to the Courses page, where the card is now gone.
    return redirect(url_for('courses.courses'))
