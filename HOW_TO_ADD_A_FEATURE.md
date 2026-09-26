# How to add your own feature

If we all edit app.py to add our own features, Git gets confused about
whose changes go where. To avoid that, each person's feature gets its
own file in the `features` folder. You will NOT need to open or
change app.py.

## Steps

1. Go to the `features` folder. Copy `courses.py` and rename the copy
   to match your feature, like `assignments.py`.

2. Open your new file. At the top, find this line:

   `courses_bp = Blueprint('courses', __name__)`

   Change the word "courses" (both times) to your feature's name.
   Example for assignments:

   `assignments_bp = Blueprint('assignments', __name__)`

3. Change the routes and the code inside them to do what your feature
   needs. A "route" is just a web page address, like `/courses`.
   Yours might be `/assignments`.

4. If your feature needs to save information (like a course, a task,
   a grade), add a new class to `models.py`, the same way `Course` is
   written there. Each class becomes its own table in the database.

5. Run the app with `python app.py` and open your new page in the
   browser to make sure it works.

That's it. You never touched app.py, so your file won't clash with
anyone else's when we combine our work.
