from flask import Flask
from flask_cors import CORS

from server.api.route import api_v1


STATIC_PATH = 'static/'


def create_app():
    # instantiate the app
    app = Flask(__name__)
    app.config.from_object(__name__)

    # static ressources
    app = Flask(__name__, static_folder=STATIC_PATH)

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    app.register_blueprint(api_v1)

    return app
