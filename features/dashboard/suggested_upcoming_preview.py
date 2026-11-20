# SSAP-12 (Bhavya): Upcoming Assignments Preview on the Dashboard.

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from models import Assignment


def suggested_upcoming_preview(user_id):
    today = datetime.now(ZoneInfo("America/New_York")).date()

    # The "This Week" box already shows today + the next 6 days,
    # so this box starts the day after that. That way the same
    # assignment isn't listed twice on the dashboard.
    after_this_week = (today + timedelta(days=7)).isoformat()

    # Get later, incomplete assignments for this student
    # (plus ones with no due date, which "This Week" never shows).
    assignments = (
        Assignment.query
        .filter_by(user_id=user_id)
        .filter(Assignment.status != "Completed")
        .filter(
            (Assignment.due_date >= after_this_week)
            | (Assignment.due_date.is_(None))
            | (Assignment.due_date == "")
        )
        .all()
    )

    # Sort assignments by deadline.
    # Assignments without a deadline appear last.
    assignments.sort(
        key=lambda assignment: assignment.due_date or "9999-12-31"
    )

    # Return the next five assignments.
    return assignments[:5]
