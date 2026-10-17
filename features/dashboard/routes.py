"""
features/dashboard/routes.py -- Dashboard: the home page. It asks each box's small file for its
information, then shows templates/dashboard/home.html.
"""
from flask import render_template, session
from . import dashboard_bp

# Each dashboard box gets its numbers from its own small file, so the
# people building different boxes never edit the same file.
# (The "suggested_" names are only suggestions. Rename a file if you
# like, then update its line below and its include in home.html.)
from .suggested_summary_cards import suggested_summary_cards
from .suggested_schedule_preview import suggested_schedule_preview
from .suggested_course_cards import suggested_course_cards
from .suggested_mini_calendar import suggested_mini_calendar
from .suggested_upcoming_preview import suggested_upcoming_preview


@dashboard_bp.route('/')
def index():
    user_id = session['user_id']

    # Collect what each box needs, then hand it all to the page.
    return render_template(
        'dashboard/home.html',
        summary_cards=suggested_summary_cards(user_id),
        schedule_preview=suggested_schedule_preview(user_id),
        course_cards=suggested_course_cards(user_id),
        mini_calendar=suggested_mini_calendar(user_id),
        upcoming_preview=suggested_upcoming_preview(user_id)
    )
