# static/css/ -- the styles

| File | What it is for | Loaded by |
|------|----------------|-----------|
| `theme.css` | Colors, fonts, and basic text. Change a color here to change the whole app. | every page |
| `layout.css` | The page frame: sidebar and signed-out screen. | every page |
| `components.css` | Pieces many features share: forms, buttons, messages, the dashed "coming soon" box. | every page |
| `dashboard.css` | Only the Dashboard. | dashboard page |
| `courses.css` | Only the Courses page. | courses page |
| `progress.css` | Only the Progress page. | progress page |

## Adding styles for your feature

1. Make `static/css/<your_feature>.css`. Use the color names from
   `theme.css`, like `color: var(--text);`.
2. Load it from your page template:

```
{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/<your_feature>.css') }}">
{% endblock %}
```

Only edit the shared files (`theme`, `layout`, `components`) if the
change really belongs to the whole app.
