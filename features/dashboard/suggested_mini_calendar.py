"""
features/dashboard/suggested_mini_calendar.py

SSAP-23:
Dashboard Mini Calendar Widget.

Shows:
- the current month
- today's date
- a dot on days that have an assignment due
- only assignments belonging to the signed-in student
"""

import calendar
from datetime import datetime
from zoneinfo import ZoneInfo

from models import Assignment


def suggested_mini_calendar(user_id):

    # Use the same timezone as the full calendar.
    today = datetime.now(
        ZoneInfo("America/New_York")
    ).date()

    year = today.year
    month = today.month

    # Example:
    # 2026-11-
    month_prefix = (
        f"{year}-{month:02d}-"
    )

    # Only get assignments for the signed-in student
    # that are due during the current month.
    assignments = (
        Assignment.query
        .filter_by(user_id=user_id)
        .filter(
            Assignment.due_date.isnot(None)
        )
        .filter(
            Assignment.due_date.like(
                f"{month_prefix}%"
            )
        )
        .all()
    )

    # Store the days that have at least one assignment.
    # Example:
    # {5, 12, 22}
    due_days = set()

    for assignment in assignments:

        if not assignment.due_date:
            continue

        try:

            due_date = datetime.strptime(
                assignment.due_date,
                "%Y-%m-%d"
            ).date()

            due_days.add(
                due_date.day
            )

        except ValueError:
            # Ignore an invalid date instead of
            # breaking the dashboard.
            continue


    # Sunday-first calendar to match a normal
    # calendar layout.
    month_calendar = calendar.Calendar(
        firstweekday=6
    )

    weeks = month_calendar.monthdayscalendar(
        year,
        month
    )


    return {

        "month_name":
            calendar.month_name[month],

        "year":
            year,

        "month":
            month,

        "today":
            today.day,

        "weeks":
            weeks,

        "due_days":
            due_days,

    }