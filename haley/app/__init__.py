import os

from flask import Flask
from flask import (
    render_template
)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True,
                static_url_path='', static_folder='./static')

    # a simple page that says hello
    @app.route('/')
    def homepage():
        items = [{
            "title": "Item 1",
            "image": "Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        }, {
            "title": "Item 2",
            "image": "Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        }, {
            "title": "Item 6",
            "image": "Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        }]
        return render_template('home.html', items=items)

    return app
