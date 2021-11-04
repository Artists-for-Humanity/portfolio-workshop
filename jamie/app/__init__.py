import os

from flask import Flask
from flask import (
    render_template
)

userInfo = {
    "stephen": {
        "age": 29,
        "address": "sdfdsf"
    },
    "jamie": {
        "age": 18
    }
}

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, static_url_path='', static_folder='./static')

    # a simple page that says hello
    @app.route('/')
    def homepage():
        items = [{
            "title": "Item 1",
            "image": "Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        }, {
            "title": "Item 2",
            "image": "Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        },
        {
            "title": "Item 6",
            "image": "Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        },{
            "title": "Item 6",
            "image": "Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        },]
        return render_template('home.html', items=items)

    @app.route('/gallery')
    def galleryPage():
        items = [{
            "title": "Item 1",
            "image": "Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        }, {
            "title": "Item 2",
            "image": "Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        },
        {
            "title": "Item 6",
            "image": "Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        },{
            "title": "Item 6",
            "image": "Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        },]
        return render_template('gallery.html', items=items)

    @app.route('/commission')
    def commisionPage():
        items = [{
            "title": "Item 1",
            "image": "Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        }, {
            "title": "Item 2",
            "image": "Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        },
        {
            "title": "Item 6",
            "image": "Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        },{
            "title": "Item 6",
            "image": "Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        },]
        return render_template('commission.html', items=items)

    @app.route('/profile/<username>/edit')
    def namePage(username):
        user = userInfo[username]
        return render_template('name.html', user=user)
    
    return app

    