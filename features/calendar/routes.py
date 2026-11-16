"""
features/calendar/routes.py -- Interactive monthly calendar with filters.
"""

import calendar as month_calendar
from datetime import date, datetime
from zoneinfo import ZoneInfo

from flask import render_template, request, session

from models import Assignment, Course
from . import calendar_bp


@calendar_bp.route('/calendar')
def calendar():
    today = datetime.now(ZoneInfo("America/New_York")).date()
    month_value = request.args.get('month', today.strftime('%Y-%m'))

    try:
        selected_month = datetime.strptime(month_value, '%Y-%m').date()
    except ValueError:
        selected_month = today.replace(day=1)

    year = selected_month.year
    month = selected_month.month

    first_day = date(year, month, 1)
    last_day = date(
        year,
        month,
        month_calendar.monthrange(year, month)[1]
    )

    user_id = session['user_id']

    # Only show courses belonging to the signed-in student.
    courses = Course.query.filter_by(
        user_id=user_id
    ).order_by(Course.name.asc()).all()

    # Read the selected filters.
    selected_course = request.args.get('course', '').strip()
    selected_status = request.args.get('status', '').strip()

    valid_statuses = ['Not Started', 'In Progress', 'Completed']

    if selected_status not in valid_statuses:
        selected_status = ''

    # Start with this student's assignments in the selected month.
    assignments_query = Assignment.query.filter_by(
        user_id=user_id
    ).filter(
        Assignment.due_date >= first_day.isoformat(),
        Assignment.due_date <= last_day.isoformat()
    )

    # Apply the course filter only if it belongs to this student.
    if selected_course:
        course = Course.query.filter_by(
            id=selected_course,
            user_id=user_id
        ).first()

        if course:
            assignments_query = assignments_query.filter_by(
                course_id=course.id
            )
        else:
            selected_course = ''

    # Apply the selected status.
    if selected_status:
        assignments_query = assignments_query.filter_by(
            status=selected_status
        )
    else:
        # Preserve the existing default behavior.
        assignments_query = assignments_query.filter(
            Assignment.status != 'Completed'
        )

    assignments = assignments_query.order_by(
        Assignment.due_date.asc()
    ).all()

    assignments_by_day = {}

    for assignment in assignments:
        try:
            due_date = date.fromisoformat(assignment.due_date)
            assignments_by_day.setdefault(
                due_date.day, []
            ).append(assignment)
        except (ValueError, TypeError):
            continue

    calendar_days = month_calendar.Calendar(
        firstweekday=6
    ).monthdayscalendar(year, month)

    previous_month = (
        selected_month.replace(day=1) - date.resolution
    ).strftime('%Y-%m')

    if month == 12:
        next_month = date(year + 1, 1, 1).strftime('%Y-%m')
    else:
        next_month = date(year, month + 1, 1).strftime('%Y-%m')

    return render_template(
        'calendar/home.html',
        year=year,
        month=month,
        month_name=selected_month.strftime('%B'),
        calendar_days=calendar_days,
        assignments_by_day=assignments_by_day,
        previous_month=previous_month,
        next_month=next_month,
        today=today,
        courses=courses,
        selected_course=selected_course,
        selected_status=selected_status
    )
