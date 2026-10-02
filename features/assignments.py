# Miczi SSAP-2 add_new_assignments
from flask import Blueprint, render_template, request, redirect, url_for
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

        assignment = Assignment(title=title)
        db.session.add(assignment)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_assignment.html')
