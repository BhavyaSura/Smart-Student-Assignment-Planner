"""
features/dashboard/friendly_dates.py -- turns "2026-11-20" into words
like "Tomorrow" or "Saturday" so the dashboard is easier to read.

Use it in any template:  {{ assignment.due_date | friendly_date }}
"""
from datetime import date, datetime
from zoneinfo import ZoneInfo

from . import dashboard_bp


def _days_until(value):
    # How many days from today until the due date (negative = past).
    # Returns None when there is no date or it isn't a real date.
    if not value:
        return None
    try:
        due = date.fromisoformat(str(value))
    except ValueError:
        return None
    today = datetime.now(ZoneInfo("America/New_York")).date()
    return (due - today).days


@dashboard_bp.app_template_filter("days_until")
def days_until(value):
    return _days_until(value)


@dashboard_bp.app_template_filter("friendly_date")
def friendly_date(value):
    days = _days_until(value)
    if days is None:
        return "No due date"
    if days == 0:
        return "Today"
    if days == 1:
        return "Tomorrow"
    if days == -1:
        return "Yesterday"
    due = date.fromisoformat(str(value))
    if 2 <= days <= 6:
        return due.strftime("%A")          # e.g. "Saturday"
    return f"{due.strftime('%b')} {due.day}"  # e.g. "Dec 3"
