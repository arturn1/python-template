
from flask import abort
from flask_restful import Resource

from system.blueprints.restapi.controllers.homeController import HomeController
from system.blueprints.restapi.helpers.token_required import token_required


class HomeResource(Resource):
    def get(self):
        try:
            response = HomeController().main()
        except:
            abort(500)

        return response, 200

    @token_required
    def post(self):
        try:
            response = HomeController().main()
        except:
            abort(500)

        return response, 201

    @token_required
    def put(self):
        try:
            response = HomeController().main()
        except:
            abort(500)

        return response, 201

    @token_required
    def delete(self):
        try:
            response = HomeController().main()
        except:
            abort(500)

        return response, 201
