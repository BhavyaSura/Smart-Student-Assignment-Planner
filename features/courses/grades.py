"""
features/courses/grades.py -- Courses: adding, editing and deleting
grade items. (SSAP-30)

  POST /courses/<id>/grades/add                 add a grade item
  GET  /courses/<id>/grades/<item_id>/edit      the edit form
  POST /courses/<id>/grades/<item_id>/edit      save the edit
  POST /courses/<id>/grades/<item_id>/delete    delete it

The grade cards and the calculator are shown on the course details
page (see course_details() in routes.py).
"""
from flask import render_template, request, redirect, url_for, session
from models import db, Course
from . import courses_bp
from .models import GradeItem


@courses_bp.app_template_filter('pct')
def pct(value):
    # A template filter: {{ 20.0|pct }} shows "20" and {{ 88.94|pct }}
    # shows "88.9". Rounds to 1 decimal and drops a pointless ".0".
    # (":g" is Python's "general" number format, which skips trailing zeros.)
    return f'{round(value, 1):g}'


def read_grade_form(course, item=None):
    # Read and check the name / weight / score boxes.
    # Returns (name, weight, score, error). error is None when it's all OK.
    name = request.form.get('name', '').strip()
    weight_text = request.form.get('weight', '').strip()
    score_text = request.form.get('score', '').strip()

    if not name:
        return name, None, None, 'Please enter a name, like "Midterm".'

    # float() turns the text "25" into the number 25.0.
    # If they typed something that isn't a number, float() fails.
    try:
        weight = float(weight_text)
    except ValueError:
        return name, None, None, 'Weight must be a number, like 25.'

    if weight <= 0 or weight > 100:
        return name, None, None, 'Weight must be between 1 and 100.'

    # All the course's weights together can't go over 100%.
    # (When editing, don't count the item's old weight.)
    other_weight = sum(
        other.weight for other in course.grade_items
        if item is None or other.id != item.id
    )
    if other_weight + weight > 100:
        left = 100 - other_weight
        return name, None, None, (
            f'That would make the weights add up to more than 100%. '
            f'You have {left:g}% left to use.'
        )

    # The score is optional: leave it empty if it isn't graded yet.
    score = None
    if score_text:
        try:
            score = float(score_text)
        except ValueError:
            return name, None, None, 'Score must be a number, like 88.'
        if score < 0 or score > 100:
            return name, None, None, 'Score must be between 0 and 100.'

    return name, weight, score, None


def find_course(course_id):
    # Only find the course if it belongs to the signed-in student.
    return Course.query.filter_by(
        id=course_id,
        user_id=session['user_id']
    ).first_or_404()


def find_grade_item(course, item_id):
    # Only find the item if it belongs to this course AND this student.
    return GradeItem.query.filter_by(
        id=item_id,
        course_id=course.id,
        user_id=session['user_id']
    ).first_or_404()


@courses_bp.route('/courses/<int:course_id>/grades/add', methods=['POST'])
def add_grade_item(course_id):
    course = find_course(course_id)
    name, weight, score, error = read_grade_form(course)

    if error:
        # Go back to the course page and show the error above the form.
        # "#grades" scrolls the page down to the grades section.
        return redirect(url_for(
            'courses.course_details', course_id=course.id, grade_error=error
        ) + '#grades')

    new_item = GradeItem(
        user_id=session['user_id'],
        course=course,
        name=name,
        weight=weight,
        score=score,
    )
    db.session.add(new_item)
    db.session.commit()

    return redirect(url_for('courses.course_details', course_id=course.id) + '#grades')


@courses_bp.route('/courses/<int:course_id>/grades/<int:item_id>/edit',
                  methods=['GET', 'POST'])
def edit_grade_item(course_id, item_id):
    course = find_course(course_id)
    item = find_grade_item(course, item_id)

    if request.method == 'POST':
        name, weight, score, error = read_grade_form(course, item)

        if error:
            return render_template('courses/grade_edit.html',
                                   course=course, item=item, error=error)

        item.name = name
        item.weight = weight
        item.score = score
        db.session.commit()

        return redirect(url_for('courses.course_details', course_id=course.id) + '#grades')

    return render_template('courses/grade_edit.html', course=course, item=item)


@courses_bp.route('/courses/<int:course_id>/grades/<int:item_id>/delete',
                  methods=['POST'])
def delete_grade_item(course_id, item_id):
    course = find_course(course_id)
    item = find_grade_item(course, item_id)

    db.session.delete(item)
    db.session.commit()

    return redirect(url_for('courses.course_details', course_id=course.id) + '#grades')
