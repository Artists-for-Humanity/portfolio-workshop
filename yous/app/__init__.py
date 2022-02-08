import os

from flask import Flask
from flask import (
    render_template
)

items = [{
    "thumbnail": "/images/TDMovieOut.0.jpg",
    "video": "/images/GrowVideo.mp4"
}]

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, static_url_path='', static_folder='./static')

    # a simple page that says hello
    @app.route('/')
    @app.route('/yous/index.html')
    @app.route('/poop')
    def homepage():
        global items
        return render_template('home.html', items=items)

    @app.route('/video/<index>')
    def video(index):
        return render_template('video.html', item=items[int(index)])
    
    return app
