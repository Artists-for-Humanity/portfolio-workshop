import os

from flask import Flask
from flask import (
    render_template
)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, static_url_path='', static_folder='./static')

    # a simple page that says hello
    @app.route('/')
    def homepage():
        items  = [{
            "name": "William C. Yu",
            "image": "/images/William C. Yu.jpeg"
        }, {
            "name": "Amie C. Gram",
            "image": "/images/Amie C. Gram .jpeg"
        }, {
            "name": "Chris Peanuts",
            "image": "/images/Leonard B. Andrews .jpeg"
        },{
            "name": "Orville M. Bober",
            "image": "/images/Orville M. Bober .jpeg"
        },{
            "name":"Jose H. Schaffer",
            "image":"/images/Jose H. Schaffer .jpeg"
        }]
        return render_template('home.html', items=items)
    
    return app
