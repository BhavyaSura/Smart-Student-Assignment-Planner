# SSAP-12 (Bhavya): Upcoming Assignments Preview on the Dashboard.

from datetime import datetime
from zoneinfo import ZoneInfo

from models import Assignment


def suggested_upcoming_preview(user_id):
    today = datetime.now(ZoneInfo("America/New_York")).date().isoformat()

    # Get upcoming and incomplete assignments for this student.
    assignments = (
        Assignment.query
        .filter_by(user_id=user_id)
        .filter(Assignment.status != "Completed")
        .filter(
            (Assignment.due_date >= today)
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
