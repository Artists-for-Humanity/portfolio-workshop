import os

from flask import Flask
from flask import render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_url_path="",
        static_folder="./static",
    )

    # a simple page that says hello
    @app.route("/")
    def nav():
        items = [{"title": ""}]
        content_box= [{"title": ""}, {"title": ""}, {"titles": ""}]
        return render_template( "homepage/home.html", items=items, content_box=content_box)

    return app
