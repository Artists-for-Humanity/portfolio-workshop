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
    # a simple page that says hello

    @app.route('/explore')
    def explorepage():
        images = [{
            "src": "images/ocean.jpg",
            "alt": "ocean img"
        }, {
            "src": "images/tan.jpg",
            "alt": "tan img"
        }, {
            "src": "images/city.jpg",
            "alt": "city img"
        }, {
            "src": "images/human.jpg",
            "alt": "human img"
        }, {
            "src": "images/portrait.jpg",
            "alt": "portrait img"
        }, {
            "src": "images/purple.jpg",
            "alt": "purple img"
        }, {
            "src": "images/supplies.jpg",
            "alt": "supplies img"
        }, {
            "src": "images/ribbon.jpg",
            "alt": "ribbon img"
        }, {
            "src": "images/black.jpg",
            "alt": "black img"
        }, {
            "src": "images/drums.jpg",
            "alt": "drums img"
        }]
        return render_template('explore.html', images=images)

    return app
