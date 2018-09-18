from os import path
from click import get_app_dir
from flask import Flask, render_template, jsonify
# from webui import ui


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    if test_config is None:
        # load default_settings. No FLASK_ENV-variable is set, but it
        # defaults to 'development'
        app.config.from_pyfile('default_settings.cfg')
        # load user_settings. Must be present as they contain the SECRET_KEY
        # and more necessary envvars
        user_settings = path.join(get_app_dir('Almanak'), 'user_settings.cfg')
        app.config.from_pyfile(user_settings)

    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # a simple page that says hello
    @app.route('/config')
    def hello():
        return render_template('subpage.html', cfg=app.config)
        # return jsonify(app.config)

    @app.route('/env')
    def env():
        return app.config.get('USER_SETTINGS_VAR', 'Missing env-key')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/subpage')
    def subpage():
        return render_template('subpage.html')

    return app
    # return WebUI(app, debug=True)
