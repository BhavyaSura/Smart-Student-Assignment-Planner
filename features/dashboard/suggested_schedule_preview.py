
"""
SSAP-24: Dashboard Schedule Widget.
Shows upcoming assignments from the Calendar.
"""

from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

from models import Assignment


def suggested_schedule_preview(user_id):
    # Use Eastern time like the rest of the dashboard, so the
    # schedule doesn't jump to tomorrow early on PythonAnywhere.
    today = datetime.now(ZoneInfo("America/New_York")).date()
    end_date = today + timedelta(days=6)

    assignments = Assignment.query.filter_by(
        user_id=user_id
    ).filter(
        Assignment.due_date >= today.isoformat(),
        Assignment.due_date <= end_date.isoformat(),
        Assignment.status != "Completed"
    ).order_by(
        Assignment.due_date.asc()
    ).all()

    schedule = []

    for assignment in assignments:
        try:
            due_date = date.fromisoformat(assignment.due_date)
        except (ValueError, TypeError):
            continue

        schedule.append({
            "title": assignment.title,
            "due_date": due_date,
            "day": due_date.strftime("%A"),
            "date_label": due_date.strftime("%b %d"),
            # Extra details for the polished schedule rows.
            "short_day": due_date.strftime("%a"),       # e.g. "Fri"
            "day_number": due_date.day,                 # e.g. 20
            "iso_date": assignment.due_date,
            "course": assignment.course.name if assignment.course else None,
            "status": assignment.status or "Not Started"
        })

    return schedule
