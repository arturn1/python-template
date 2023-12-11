from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS


from system.blueprints.restapi.routers.homeResource import HomeResource
from system.blueprints.restapi.services.headers import set as headers_set

bp = Blueprint("restapi", __name__, url_prefix="/v1")


CORS(bp, resources=r'/v1/*')

api = Api(bp)

api.add_resource(HomeResource, "/")

headers_set({})


def init_app(app):
    app.register_blueprint(bp)
