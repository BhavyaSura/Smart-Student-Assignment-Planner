from datetime import datetime, timedelta

from models import Assignment

from zoneinfo import ZoneInfo

def suggested_summary_cards(user_id):
    today = datetime.now(ZoneInfo("America/New_York")).date()
    seven_days_from_now = today + timedelta(days=7)

    assignments = Assignment.query.filter_by(user_id=user_id).all()

    total_assignments = len(assignments)
    completed = 0
    due_within_7_days = 0
    overdue = 0

    for assignment in assignments:
        if assignment.status == "Completed":
            completed += 1

        if not assignment.due_date:
            continue

        try:
            due_date = datetime.strptime(
                assignment.due_date,
                "%Y-%m-%d"
            ).date()
        except ValueError:
            continue

        if (
            assignment.status != "Completed"
            and today <= due_date <= seven_days_from_now
        ):
            due_within_7_days += 1

        if (
            assignment.status != "Completed"
            and due_date < today
        ):
            overdue += 1

    return {
        "total": total_assignments,
        "completed": completed,
        "due_within_7_days": due_within_7_days,
        "overdue": overdue
    }