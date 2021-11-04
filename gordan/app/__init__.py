import os

from flask import Flask
from flask import (render_template)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__,
                instance_relative_config=True,
                static_url_path='',
                static_folder='./static')

    # a simple page that says hello
    @app.route('/')
    @app.route('/portfolio')
    def portfoliopage():
        items = [{
            "text":
            '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sem quam, elementum quis felis sit
                amet,
                gravida ullamcorper leo. Morbi id odio nec libero feugiat auctor. Etiam sollicitudin ultricies magna
                vulputate
                pulvinar. Integer gravida eros sit amet consequat placerat. Curabitur faucibus, metus id gravida dictum,
                mi tortor euismod libero, a laoreet mauris quam non erat. Nullam molestie ex accumsan neque blandit, et
                finibus
                dui convallis. Proin ullamcorper lacus sit amet erat mollis, vel aliquet mi rutrum. Etiam laoreet
                aliquam arcu
                et
                rutrum. Pellentesque posuere pulvinar enim, nec ornare orci. Suspendisse vestibulum mi ante, a congue
                lacus
                euismod
                ac. Cras sagittis eleifend diam sed blandit. Etiam tempor justo urna. Pellentesque euismod placerat
                purus,
                nec aliquam massa ullamcorper nec. Morbi magna nisl, fermentum suscipit eros et, elementum tincidunt
                nulla.
                In ligula massa, rhoncus quis enim eget, varius egestas nunc.''',
            "image":
            "/images/Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        }, {
            "text":
            '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sem quam, elementum quis felis sit
                amet,
                gravida ullamcorper leo. Morbi id odio nec libero feugiat auctor. Etiam sollicitudin ultricies magna
                vulputate
                pulvinar. Integer gravida eros sit amet consequat placerat. Curabitur faucibus, metus id gravida dictum,
                mi tortor euismod libero, a laoreet mauris quam non erat. Nullam molestie ex accumsan neque blandit, et
                finibus
                dui convallis. Proin ullamcorper lacus sit amet erat mollis, vel aliquet mi rutrum. Etiam laoreet
                aliquam arcu
                et
                rutrum. Pellentesque posuere pulvinar enim, nec ornare orci. Suspendisse vestibulum mi ante, a congue
                lacus
                euismod
                ac. Cras sagittis eleifend diam sed blandit. Etiam tempor justo urna. Pellentesque euismod placerat
                purus,
                nec aliquam massa ullamcorper nec. Morbi magna nisl, fermentum suscipit eros et, elementum tincidunt
                nulla.
                In ligula massa, rhoncus quis enim eget, varius egestas nunc.''',
            "image":
            "/images/Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        }, {
            "text":
            '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sem quam, elementum quis felis sit
                amet,
                gravida ullamcorper leo. Morbi id odio nec libero feugiat auctor. Etiam sollicitudin ultricies magna
                vulputate
                pulvinar. Integer gravida eros sit amet consequat placerat. Curabitur faucibus, metus id gravida dictum,
                mi tortor euismod libero, a laoreet mauris quam non erat. Nullam molestie ex accumsan neque blandit, et
                finibus
                dui convallis. Proin ullamcorper lacus sit amet erat mollis, vel aliquet mi rutrum. Etiam laoreet
                aliquam arcu
                et
                rutrum. Pellentesque posuere pulvinar enim, nec ornare orci. Suspendisse vestibulum mi ante, a congue
                lacus
                euismod
                ac. Cras sagittis eleifend diam sed blandit. Etiam tempor justo urna. Pellentesque euismod placerat
                purus,
                nec aliquam massa ullamcorper nec. Morbi magna nisl, fermentum suscipit eros et, elementum tincidunt
                nulla.
                In ligula massa, rhoncus quis enim eget, varius egestas nunc.''',
            "image":
            "/images/Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        }, {
            "text":
            '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sem quam, elementum quis felis sit
                amet,
                gravida ullamcorper leo. Morbi id odio nec libero feugiat auctor. Etiam sollicitudin ultricies magna
                vulputate
                pulvinar. Integer gravida eros sit amet consequat placerat. Curabitur faucibus, metus id gravida dictum,
                mi tortor euismod libero, a laoreet mauris quam non erat. Nullam molestie ex accumsan neque blandit, et
                finibus
                dui convallis. Proin ullamcorper lacus sit amet erat mollis, vel aliquet mi rutrum. Etiam laoreet
                aliquam arcu
                et
                rutrum. Pellentesque posuere pulvinar enim, nec ornare orci. Suspendisse vestibulum mi ante, a congue
                lacus
                euismod
                ac. Cras sagittis eleifend diam sed blandit. Etiam tempor justo urna. Pellentesque euismod placerat
                purus,
                nec aliquam massa ullamcorper nec. Morbi magna nisl, fermentum suscipit eros et, elementum tincidunt
                nulla.
                In ligula massa, rhoncus quis enim eget, varius egestas nunc.''',
            "image":
            "/images/Mai, Shu Ru. Still Life Hunger Games Pear Green Table.jpg"
        }]
        return render_template('/pages/portfolio.html', items=items)

    return app
