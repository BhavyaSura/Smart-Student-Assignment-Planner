# SSAP-10 (Jiovany): the course cards on the dashboard.
#
# The real work happens in features/courses/progress.py, which the
# Courses page uses too, so both pages always show the same numbers.
from features.courses.progress import course_cards

# The dashboard row only has room for 4 cards.
CARDS_ON_DASHBOARD = 4


def suggested_course_cards(user_id):
    cards = course_cards(user_id)

    return {
        'cards': cards[:CARDS_ON_DASHBOARD],   # the first 4 courses
        'total': len(cards),                   # used for "View all (6)"
    }
