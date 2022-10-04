import string
from tokenize import String


class Request:
    def __init__(self):
        self._name = ""
        self._method = ""
        self._url = ""
    
    @property
    def name(self):
        return self._name

    @property
    def method(self):
        return self._method

    @property
    def url(self):
        return self._url

    @name.setter
    def name(self, name: string):
        self._name = name

    @method.setter
    def method(self, method: string):
        self._method = method

    @url.setter
    def url(self, url: string):
        self._url = url

    def __str__(self):
        return f"name: {self.name}\nmethod: {self.method}\nurl: {self.url}\n"

    def call_request(self):
        print("Go call the appropriate class method!")