import HttpRequest, Get

class Factory:
    def __init__(self):
        self._request = None
    
    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, request: HttpRequest.Request):
        self._request = request

    def construct_request(self):
        if (self._request):
            if self._request.method == 'GET':
                request = Get.Request()
                request.url = self._request.url
                request.name = self._request.name
                return request
            elif  self._request.method == 'POST':
                # TODO: Implement POST
                return None
            else:
                return None
        else:
            raise Exception("Must have base request")
        