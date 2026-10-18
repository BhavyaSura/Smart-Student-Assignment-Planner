# Miczi SSAP-2 add_new_assignments
from flask import Blueprint, render_template, request, redirect, url_for,session
from models import db, Assignment


assignments_bp = Blueprint('assignments', __name__)


@assignments_bp.route('/add-assignment', methods=['GET', 'POST'])
def add_assignment():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()

        if not title:
            return render_template(
                'add_assignment.html',
                error='Please enter an assignment name.'
            )

        assignment = Assignment(title=title, user_id=session['user_id'])
        db.session.add(assignment)
        db.session.commit()

        # Send them to the list so they can actually see what they added.
        return redirect(url_for('upcoming_assignments.upcoming_assignments'))

    return render_template('add_assignment.html')
