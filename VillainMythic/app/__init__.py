import os

from flask import Flask
from flask import render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_url_path="",
        static_folder="static",
    )

    # a simple page that says hello
    @app.route("/")
    def homepage():
        items = [{"title": "Item 1"}, {"title": "Item 2"}]
        return render_template("index.html", items=items)

    return app
