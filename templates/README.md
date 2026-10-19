# templates/ -- the HTML pages

There is one folder per feature, with the same name as the folder in
`features/`. So the page code for Courses is in `features/courses/` and
its HTML is in `templates/courses/`.

```
templates/
  base.html      The frame around every page (sidebar, styles). Rarely edited.
  dashboard/     Dashboard. Files starting with "suggested_" are the boxes on it.
  courses/       Courses pages
  assignments/   Assignment pages
  calendar/      Calendar page
  progress/      Progress page
  shared/        Small pieces used by more than one page (the "Due Soon" box)
  auth/          Sign in / create account
```

* A page starts with `{% extends "base.html" %}` and puts its content
  inside `{% block content %}`.
* A feature that needs its own styles adds them in
  `{% block extra_css %}` (see `static/css/README.md`).
* Files starting with `suggested_` in the dashboard folder are small pieces
  that `home.html` includes. Their names are only suggestions.
