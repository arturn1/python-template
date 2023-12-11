header = {}


def set(headers):
    version = headers.get("version")
    token = headers.get("token")

    header["version"] = version
    header["content-type"] = "application/json"
    header["Authorization"] = token


def get():
    return header
