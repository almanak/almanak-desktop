import os
from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='',
    # )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        # app.config.from_pyfile('config.py', silent=True)
        # I'm just using direct config for now
        app.config.from_mapping(
            TESTVAR = 'testvar',
        )
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    # used to place a db-file in the tutorial
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return app.config.get('TESTVAR', 'no testvar')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/subpage')
    def subpage():
        return render_template('subpage.html')

    return app