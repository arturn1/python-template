from flask import Flask
from dynaconf import FlaskDynaconf

from system.extension import configuration


def create_app():
    app = Flask(__name__)
    app.config.from_object("configurations.DevelopmentConfig")

    if app.config["ENV"] == "development":
        app.debug = True
    else:
        app.debug = False

    FlaskDynaconf(app)

    configuration.init_app(app)
    configuration.load_extensions(app)

    return app
