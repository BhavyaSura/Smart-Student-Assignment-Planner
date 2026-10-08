# SSAP-5 - Course Feature
# Allows users to view and add courses to the planner.


from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Course

# This creates a small, separate group of web pages just for courses.
courses_bp = Blueprint('courses', __name__)


@courses_bp.route('/courses')
def courses():
    # Get every course that has been saved in the database so far.
    all_courses = Course.query.all()
    # Show the courses.html page and hand it the list of courses.
    return render_template('courses.html', courses=all_courses)


@courses_bp.route('/courses/add', methods=['POST'])
def add_course():
    # This runs when someone submits the "Add Course" form.
    name = request.form.get('name')
    code = request.form.get('code')
    instructor = request.form.get('instructor')

    # If they didn't type a course name, don't save anything.
    # Instead, show the page again with a message telling them why.
    if not name:
        all_courses = Course.query.all()
        return render_template(
            'courses.html',
            courses=all_courses,
            error='Please enter a course name.'
        )

    # Save the new course to the database.
    new_course = Course(name=name, code=code, instructor=instructor)
    db.session.add(new_course)   # put the new course in line to be saved
    db.session.commit()          

    # Send the person back to the courses page so they can see it added.
    return redirect(url_for('courses.courses'))
