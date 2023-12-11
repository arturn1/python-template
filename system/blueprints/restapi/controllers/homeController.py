from ..services.request import Requests

from ..models import Response

from ..enums.message import Message

request = Requests()


class HomeController:
    def __init__(self):

        self.response = {
            "status": 200,
            "msg": Message.SUCCESS_DATA.value,
            "data": None,
        }

    def main(self) -> Response:
        return self.response
