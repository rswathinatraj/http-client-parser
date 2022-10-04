import HttpRequest

class Request(HttpRequest.Request):
    def __init__(self):
        self.method = "POST"
        self.body = ""
        super().__init__()