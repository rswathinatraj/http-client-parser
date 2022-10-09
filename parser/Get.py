import HttpRequest
import requests
import re

class Request(HttpRequest.Request):
    def __init__(self):
        self.method = "GET"
        super().__init__()

    def replace_env_vars(self, env_vars):
        vars = re.findall(r"\{\{([a-zA-Z]*)\}\}", self.url)
        if vars and len(vars):
            for var in vars:
                print(var)
                self.url = self.url.replace("{{%s}}" % var, env_vars.get(var))

    def call_request(self):
        results = requests.get(url = self.url)
        return results.json()