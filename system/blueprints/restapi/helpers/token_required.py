from functools import wraps
from flask import request

from system.blueprints.restapi.enums.message import Message
from system.blueprints.restapi.services.request import Requests

from system.blueprints.restapi.services.headers import set as headers_set


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = request.headers.get("Authorization")
        version = request.headers.get("version")

        if not token:
            res = {
                "msg": Message.MISSING_TOKEN.value,
                "status": 401,
                "data": None
            }

            return res, 401

        if not version:
            res = {
                "msg": Message.MISSING_VERSION.value,
                "status": 400,
                "data": None
            }

            return res, 400

        try:
            headers = {"version": version, "token": token}
            headers_set(headers)

            auth = Requests().api(token)

            if (auth["status"] == 200):
                pass
            else:
                res = {
                    "msg": Message.FORBIDDEN.value,
                    "status": 403,
                    "data": None
                }

                return res, 403
        except Exception as error:
            res = {
                "msg": Message.INVALID_TOKEN.value,
                "status": 400,
                "data": None
            }

            return res, 400
        return f(*args, **kwargs)

    return decorated
