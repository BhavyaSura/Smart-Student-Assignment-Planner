"""
features/courses/progress.py -- Courses: works out how far along each
course is. (SSAP-10)

The Courses page and the Dashboard's course cards both use this, so the
math lives in one place.
"""
from models import Course

# How many cover designs there are. Each one is a class in
# static/css/components.css, named course-theme-0 through course-theme-5,
# and uses an image from static/img/covers/.
NUMBER_OF_ARTS = 6


def course_progress(course):
    # Count this course's assignments and how many are Completed.
    total = len(course.assignments)
    completed = sum(
        1 for assignment in course.assignments
        if assignment.status == 'Completed'
    )

    # Turn it into a percentage. A course with no assignments is 0%,
    # so we never divide by zero.
    if total > 0:
        percent = round((completed / total) * 100)
    else:
        percent = 0

    return {'total': total, 'completed': completed, 'percent': percent}


def course_cards(user_id):
    # Get this student's courses, oldest first, and attach each one's
    # progress and cover design. The template only has to show them.
    courses = Course.query.filter_by(user_id=user_id).order_by(Course.id).all()

    cards = []
    for course in courses:
        cards.append({
            'course': course,
            'progress': course_progress(course),
            # The course's id picks its cover, so a course keeps the same
            # cover every time the page loads.
            'art': course.id % NUMBER_OF_ARTS,
        })
    return cards
