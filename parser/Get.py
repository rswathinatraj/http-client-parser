import HttpRequest
import requests

class Request(HttpRequest.Request):
    def __init__(self):
        self.method = "GET"
        super().__init__()

    def call_request(self):
        results = requests.get(url = self.url)
        return results.json()