from datetime import datetime, timedelta

from models import Assignment, User

from zoneinfo import ZoneInfo

def suggested_greeting(user_id):
    user = User.query.get(user_id)

    # Choose greeting based on the current time.
    current_hour = datetime.now(ZoneInfo("America/New_York")).hour

    if current_hour < 12:
        greeting_text = "Good morning"
    elif current_hour < 18:
        greeting_text = "Good afternoon"
    else:
        greeting_text = "Good evening"

    # The current User model only stores email, so use the
    # part before @ as a friendly display name.
    display_name = "Student"

    if user and user.email:
        display_name = user.email.split("@")[0]
        display_name = display_name.replace(".", " ").replace("_", " ")
        display_name = display_name.title()

    today = datetime.now(ZoneInfo("America/New_York")).date()
    seven_days_from_now = today + timedelta(days=7)

    assignments = Assignment.query.filter_by(user_id=user_id).all()

    due_this_week = 0

    for assignment in assignments:
        if not assignment.due_date:
            continue

        if assignment.status == "Completed":
            continue

        try:
            due_date = datetime.strptime(
                assignment.due_date,
                "%Y-%m-%d"
            ).date()

            if today <= due_date <= seven_days_from_now:
                due_this_week += 1

        except ValueError:
            continue

    if due_this_week == 0:
        assignment_message = "You have no assignments due in the next 7 days."
    elif due_this_week == 1:
        assignment_message = "You have 1 assignment due in the next 7 days."
    else:
        assignment_message = (
            f"You have {due_this_week} assignments due in the next 7 days."
        )

    return {
        "greeting": f"{greeting_text}, {display_name}!",
        "message": assignment_message
    }
