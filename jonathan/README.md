# First time setting up

From inside the `/jonathan` folder run these commands in Terminal:

- `python3 -m venv venv`
- `. venv/bin/activate`
- `pip install Flask`

# Running

From inside the `/jonathan` folder run these commands from the Terminal:

- `. venv/bin/activate`
- `export FLASK_ENV=development`
- `export FLASK_APP=app`
- `flask run`

' {% for item in items %}
      {% include 'item.html' %}
      {% endfor %} '