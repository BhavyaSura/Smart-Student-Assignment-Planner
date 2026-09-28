from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Assignment

assignments_bp = Blueprint(
    'assignments',
    __name__,
    url_prefix='/assignments'
)


@assignments_bp.route('/')
def assignments():
    assignments = Assignment.query.order_by(
        Assignment.due_date.asc()
    ).all()

    return render_template(
        'assignments.html',
        assignments=assignments
    )


@assignments_bp.route('/add', methods=['POST'])
def add_assignment():

    name = request.form['name']
    course = request.form['course']
    due_date = request.form['due_date']
    priority = request.form['priority']
    estimated_time = request.form['estimated_time']

    new_assignment = Assignment(
        name=name,
        course=course,
        due_date=due_date,
        priority=priority,
        estimated_time=estimated_time
    )

    db.session.add(new_assignment)
    db.session.commit()

    return redirect(url_for('assignments.assignments'))