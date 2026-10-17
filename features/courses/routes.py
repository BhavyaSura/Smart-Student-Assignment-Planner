"""
features/courses/routes.py -- Courses: the page of course squares, plus the form that adds a course.
"""
# SSAP-5 - Course Feature
# Allows users to view and add courses to the planner.

from flask import render_template, request, redirect, url_for, session
from models import db, Course
from . import courses_bp


@courses_bp.route('/courses')
def courses():
    # Get every course this student has saved so far.
    all_courses = Course.query.filter_by(user_id=session['user_id']).all()
    # Show the courses page and hand it the list of courses.
    return render_template('courses/courses.html', courses=all_courses)


@courses_bp.route('/courses/new')
def new_course():
    # The "Add a course" square on the courses page leads here.
    return render_template('courses/add.html')


@courses_bp.route('/courses/add', methods=['POST'])
def add_course():
    # This runs when someone submits the "Add Course" form.
    # .strip() removes extra spaces, so a name of only spaces counts as empty.
    name = request.form.get('name', '').strip()
    code = request.form.get('code', '').strip()
    instructor = request.form.get('instructor', '').strip()

    # If they didn't type a course name, don't save anything.
    # Instead, show the form again with a message telling them why,
    # and keep what they already typed.
    if not name:
        return render_template(
            'courses/add.html',
            error='Please enter a course name.',
            code=code,
            instructor=instructor
        )

    # Save the new course to the database.
    new_course = Course(name=name, code=code, instructor=instructor,
                        user_id=session['user_id']
                        )
    db.session.add(new_course)   # put the new course in line to be saved
    db.session.commit()

    # Send the person back to the courses page so they can see it added.
    return redirect(url_for('courses.courses'))
