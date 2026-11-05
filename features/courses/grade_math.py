"""
features/courses/grade_math.py -- Courses: all the grade math.
(SSAP-30 Course Grade Tracking, SSAP-32 Grade Needed Calculator)

These functions only do math. They don't touch the database or Flask,
so they are easy to read and easy to test.

Example (the numbers from our mockup):
    Homework   20%  scored 92
    Quiz 1     10%  scored 85
    Midterm    25%  scored 88
    Project    20%  not graded yet
    Final      25%  not graded yet

    points earned = 20*92 + 10*85 + 25*88 = 4890
    graded weight = 20 + 10 + 25 = 55
    current grade = 4890 / 55 = 88.9%  -> B
"""

# The choices in the "To get:" dropdown.
TARGET_CHOICES = [80, 90, 95, 100]
DEFAULT_TARGET = 90


def letter_grade(percent):
    # 90+ A, 80+ B, 70+ C, 60+ D, anything lower is F.
    if percent >= 90:
        return 'A'
    if percent >= 80:
        return 'B'
    if percent >= 70:
        return 'C'
    if percent >= 60:
        return 'D'
    return 'F'


def grade_summary(grade_items):
    # Split the items into graded (has a score) and ungraded (no score yet).
    graded = [item for item in grade_items if item.score is not None]
    ungraded = [item for item in grade_items if item.score is None]

    graded_weight = sum(item.weight for item in graded)
    remaining_weight = sum(item.weight for item in ungraded)
    total_weight = graded_weight + remaining_weight

    # weight x score for every graded item, added up.
    points_earned = sum(item.weight * item.score for item in graded)

    # Current grade = points earned / graded weight.
    # If nothing is graded yet there is no grade, so we use None.
    if graded_weight > 0:
        current = round(points_earned / graded_weight, 1)
        letter = letter_grade(current)
    else:
        current = None
        letter = None

    # Completion = how much of the total weight has been graded.
    if total_weight > 0:
        completion = round(graded_weight / total_weight * 100)
    else:
        completion = 0

    return {
        'current': current,                 # e.g. 88.9  (or None)
        'letter': letter,                   # e.g. 'B'   (or None)
        'completion': completion,           # e.g. 55
        'graded_count': len(graded),        # e.g. 3
        'total_count': len(grade_items),    # e.g. 5
        'ungraded': ungraded,               # the items still to be graded
        'remaining_weight': remaining_weight,   # e.g. 45
        'total_weight': total_weight,           # should be 100 when all items are added
        'points_earned': points_earned,         # e.g. 4890
    }


def grade_needed(summary, target):
    # Needed = (target x 100 - points earned) / remaining weight
    # Example: (90 x 100 - 4890) / 45 = 91.3
    remaining = summary['remaining_weight']

    # Everything is graded, so there is nothing left to work toward.
    # (This also avoids dividing by zero.)
    if remaining == 0:
        return {'all_graded': True}

    needed = (target * 100 - summary['points_earned']) / remaining

    # Pick the badge.
    if needed > 100:
        badge = 'Not possible'
        level = 'danger'      # red
    elif needed > 90:
        badge = 'Challenging'
        level = 'warning'     # amber
    else:
        badge = 'On track'
        level = 'success'     # green

    return {
        'all_graded': False,
        # A negative number means the target is already locked in,
        # so we show 0% instead of something like -12%.
        'needed': max(round(needed, 1), 0),
        'badge': badge,
        'level': level,
        'remaining_weight': remaining,
    }
