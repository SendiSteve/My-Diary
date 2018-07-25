from flask import Flask
from flask_restful import Api
from config import app_config
from app.views import EntryList, EntryResource


def create_app():
    """This function is the application factory"""

    # instantiate flask app
    my_app = Flask(__name__, instance_relative_config=True)
    return my_app


app = create_app()
api = Api(app)

# import config settings into the application
app.config.from_object(app_config['development'])
api.add_resource(EntryList, '/api/v1/entries')
api.add_resource(EntryResource, '/api/v1/entries/<entry_id>')
