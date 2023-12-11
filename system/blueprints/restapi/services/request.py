import os
import requests

from system.blueprints.restapi.services.headers import get as headers_get
from system.blueprints.restapi.enums.message import Message


url = os.environ["BASE_URL"]


class Requests:
    def api(self, token):

        header = headers_get()

        header["Authorization"] = token

        # response = requests.get(f"{url}/auth", headers=header)

        return Message.DEVELOPER
        # return response.json()
