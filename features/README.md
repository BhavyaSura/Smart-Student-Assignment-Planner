# features/ -- one folder per feature

Each folder here is one feature, and each feature owns one button in the
left menu. Because every person works inside their own folder, we almost
never edit the same file, so Git merges are easy.

```
features/
  dashboard/     Dashboard page (+ one small file per dashboard box)
  courses/       Courses page and the "add a course" form
  assignments/   Upcoming, add, details and delete pages
  calendar/      Calendar (SSAP-19, empty for now)
  progress/      Progress overview (SSAP-9)
  auth/          Create account / sign in / sign out (no menu button)
```

## What is inside a feature folder

| File | What it is for |
|------|----------------|
| `__init__.py` | The front door. Creates the Blueprint (the group of pages), describes the sidebar button (`NAV`), and loads the page files. |
| `routes.py` (or several page files) | The pages: each `@xxx_bp.route('/address')` function is one web page. |
| `models.py` (optional) | Database tables that only your feature uses. Import it in `__init__.py`. |

## The three rules

1. Every feature folder needs an `__init__.py`.
2. The `from . import ...` line stays BELOW the Blueprint line.
3. One Blueprint per folder. Page files use `from . import xxx_bp`.

Full steps: see `HOW_TO_ADD_A_FEATURE.md` in the main folder.
