"""
features/calendar/routes.py -- Interactive monthly calendar.
"""

import calendar as month_calendar
from datetime import date, datetime

from flask import render_template, request, session

from models import Assignment
from . import calendar_bp


@calendar_bp.route('/calendar')
def calendar():
    today = date.today()
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

    assignments = Assignment.query.filter_by(
        user_id=session['user_id']
    ).filter(
        Assignment.due_date >= first_day.isoformat(),
        Assignment.due_date <= last_day.isoformat(),
        Assignment.status != 'Completed'
    ).order_by(Assignment.due_date.asc()).all()

    assignments_by_day = {}

    for assignment in assignments:
        try:
            due_date = date.fromisoformat(assignment.due_date)
            assignments_by_day.setdefault(due_date.day, []).append(assignment)
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
        today=today
    )