import json
from abc import abstractmethod


class Response:
    @abstractmethod
    def fromJson(status, msg, data):
        datas = {
            "status": status,
            "msg": msg,
            "data": data,
        }

        return datas

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
