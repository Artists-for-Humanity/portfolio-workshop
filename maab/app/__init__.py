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
            "title1": "Item 1",
            "title2": "",
            "title3": "",
            "image": "images/girl.jpeg"
        }]
        return render_template('home.html', items=items)

    return app
