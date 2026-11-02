"""
features/courses/routes.py -- Courses: the page of course cards, the form that
adds a course, and the page that shows one course's details.
"""
# SSAP-5 - Course Feature
# Allows users to view and add courses to the planner.
# SSAP-10 - Course cards with progress, plus a course details page.

from flask import render_template, request, redirect, url_for, session
from models import db, Course
from . import courses_bp
from .progress import course_cards, course_progress, NUMBER_OF_ARTS


@courses_bp.route('/courses')
def courses():
    # Get every course this student has saved, with its progress and cover art.
    cards = course_cards(session['user_id'])
    # Show the courses page and hand it the list of cards.
    return render_template('courses/courses.html', cards=cards)


@courses_bp.route('/courses/<int:course_id>')
def course_details(course_id):
    # Clicking a course card opens this page.
    # Filtering by user_id means a student can only open their OWN
    # course. Anyone else gets a "404 Not Found" page.
    course = Course.query.filter_by(
        id=course_id,
        user_id=session['user_id']
    ).first_or_404()

    # Show this course's assignments, earliest due date first.
    # Assignments with no due date go at the end.
    assignments = sorted(
        course.assignments,
        key=lambda assignment: assignment.due_date or '9999-12-31'
    )

    return render_template(
        'courses/details.html',
        course=course,
        assignments=assignments,
        progress=course_progress(course),
        art=course.id % NUMBER_OF_ARTS
    )


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
