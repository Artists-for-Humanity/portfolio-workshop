import os

from flask import Flask, app
from flask import render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_url_path="",
        static_folder="./static",
    )
    app.config.from_mapping(
         DATABASE=os.path.join(app.instance_path, 'data.sqlite'
    ))
    app.config.from_pyfile('config.py', silent=True)
   
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route("/")
    def nav():
        nav = [{"title": ""}]
        content_box= [{"title": ""}, {"title": ""}, {"titles": ""}]
        return render_template( "homepage/home.html", nav=nav, content_box=content_box)
    
    @app.route("/profile")
    def prof():
        nav = [{"title": ""}]
        userpfp= [{"title": ""}]
        userbio= [{"title": ""}]
        usercontent=[{"title": ""}]
        return render_template( "profile/profile.html", userpfp=userpfp, userbio=userbio, nav=nav, usercontent=usercontent)
    
    return app