from flask import Flask
from flask_restful import Api
from config import app_config


def create_app():
    """This function is the application factory"""

    # instantiate flask app
    my_app = Flask(__name__, instance_relative_config=True)
    return my_app


app = create_app()


# import config settings into the application
app.config.from_object(app_config['development'])
