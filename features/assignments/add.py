"""
features/assignments/add.py -- Assignments: the "Add new assignment" page (form + saving).
"""
# Miczi SSAP-2 add_new_assignments
from flask import render_template, request, redirect, url_for, session
from models import db, Assignment
from . import assignments_bp


@assignments_bp.route('/add-assignment', methods=['GET', 'POST'])
def add_assignment():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()

        if not title:
            return render_template(
                'assignments/add.html',
                error='Please enter an assignment name.'
            )

        assignment = Assignment(title=title, user_id=session['user_id'])
        db.session.add(assignment)
        db.session.commit()

        # Send them to the list so they can actually see what they added.
        return redirect(url_for('assignments.upcoming_assignments'))

    return render_template('assignments/add.html')
