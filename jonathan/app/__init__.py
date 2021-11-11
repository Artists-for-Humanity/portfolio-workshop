import os

from flask import Flask
from flask import (
    render_template
)
people  = [{
    "name": "Manuel D. Kirts",
    "image":"/images/Manuel D. Kirts.jpeg"
},{
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

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, static_url_path='', static_folder='./static')

    # a simple page that says hello
    @app.route('/')
    def homepage():
        return render_template('home.html', people=people[:3])

    @app.route('/people')
    def peoplepage():
        return render_template('people.html', people=people)

    @app.route('/people/<id>')
    def personpage(id):
        person = people[int(id)]
        return render_template('profile.html', person=person)
    
    @app.route("/halloween")
    def halloweenpage(): 
        return render_template('halloween.html')


    return app
