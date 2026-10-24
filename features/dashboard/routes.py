"""
features/dashboard/routes.py — Dashboard: the home page.
Each dashboard section gets its information from its own small file.
"""

from flask import render_template, session

from . import dashboard_bp
from .greeting import suggested_greeting
from .summary_cards import suggested_summary_cards
from .suggested_schedule_preview import suggested_schedule_preview
from .suggested_course_cards import suggested_course_cards
from .suggested_mini_calendar import suggested_mini_calendar
from .suggested_upcoming_preview import suggested_upcoming_preview
from .due_soon_alert import due_soon_alert


@dashboard_bp.route("/")
def index():
    user_id = session["user_id"]

    return render_template(
        "dashboard/home.html",

        # SSAP-6
        greeting=suggested_greeting(user_id),

        # Other dashboard features
        summary_cards=suggested_summary_cards(user_id),
        schedule_preview=suggested_schedule_preview(user_id),
        course_cards=suggested_course_cards(user_id),
        mini_calendar=suggested_mini_calendar(user_id),
        upcoming_preview=suggested_upcoming_preview(user_id),
        due_soon=due_soon_alert(user_id)
    )
