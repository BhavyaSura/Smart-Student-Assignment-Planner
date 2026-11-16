"""
features/settings/routes.py -- Settings home page.
"""
from flask_wtf.csrf import validate_csrf, ValidationError
from flask import render_template, session, request, redirect, url_for, flash
from models import db, Assignment, Course
from features.courses.models import GradeItem
from . import settings_bp
from .models import UserSettings


@settings_bp.route('/', methods=['GET', 'POST'])
def settings():
    # Only signed-in students can access Settings.
    user_id = session.get('user_id')

    if user_id is None:
        return redirect(url_for('auth.login'))

    # Find this student's settings.
    user_settings = UserSettings.query.filter_by(
        user_id=user_id
    ).first()

    # Create settings if this student doesn't have any yet.
    if user_settings is None:
        user_settings = UserSettings(user_id=user_id)
        db.session.add(user_settings)
        db.session.commit()

    
    # Save student settings.
    if request.method == 'POST':
        setting_type = request.form.get('setting_type')

        if setting_type == 'hide_completed':
            user_settings.hide_completed = (
                request.form.get('hide_completed') == 'on'
            )

            # Save the Due Soon Reminder preference.
            due_soon_days = request.form.get(
                'due_soon_days', '3'
            )

            if due_soon_days in ('1', '3', '7'):
                user_settings.due_soon_days = int(due_soon_days)
                db.session.commit()
                flash('Preferences updated successfully!')
            else:
                flash('Please select a valid reminder window.')

        elif setting_type in (None, 'display_name'):
            # Save the student's display name.
            display_name = request.form.get(
                'display_name', ''
            ).strip()

            if len(display_name) > 100:
                flash('Display name must be 100 characters or fewer.')
            else:
                user_settings.display_name = display_name or None
                db.session.commit()
                flash('Display name updated successfully!')

        return redirect(url_for('settings.settings'))

    return render_template(
        'settings/home.html',
        user_settings=user_settings
    )
@settings_bp.route('/reset-data/', methods=['POST'])
def reset_data():
    # Only signed-in students can reset their data.
    user_id = session.get('user_id')

    if user_id is None:
        return redirect(url_for('auth.login'))
     # Verify that this request came from a valid Settings form.
    try:
        validate_csrf(request.form.get('csrf_token', ''))
    except ValidationError:
        flash('Security verification failed. Please try again.')
        return redirect(url_for('settings.settings'))
    
    # Require explicit confirmation before deleting any data.
    confirmation = request.form.get('reset_confirmation', '').strip()

    if confirmation != 'RESET':
        flash('Data was not deleted. Type RESET to confirm.')
        return redirect(url_for('settings.settings'))
    # Delete only records owned by this student.
    try:
        GradeItem.query.filter_by(user_id=user_id).delete(
            synchronize_session=False
        )

        Assignment.query.filter_by(user_id=user_id).delete(
            synchronize_session=False
        )

        Course.query.filter_by(user_id=user_id).delete(
            synchronize_session=False
        )

        db.session.commit()
        flash('Your assignments, courses, and grades have been reset.')

    except Exception:
        db.session.rollback()
        flash('Unable to reset your data. No changes were saved.')

    return redirect(url_for('settings.settings'))

