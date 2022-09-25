import re
import requests
import sys, getopt

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
    def name(self, name):
        self._name = name

    @method.setter
    def method(self, method):
        self._method = method

    @url.setter
    def url(self, url):
        self._url = url

    def __str__(self):
        return f"name: {self.name}\nmethod: {self.method}\nurl: {self.url}\n"

def extract_name(line):
    name = re.search(r"([#]{3}) ([a-zA-Z]*)", line)
    return name.group(2)

def extract_method_url(line):
    method_url = re.search(r"([GET|POST|DELETE|PUT]+) (.*)", line)
    return method_url.groups()
        

def parse_request(file):
    request = Request()
    while (True):
        line = file.readline()
        if (line):
            if (not re.match(r"\n", line)):
                if (line.startswith("###")):
                    name = extract_name(line)
                    request.name = name
                else:
                    if (request.name):
                        method_url = extract_method_url(line)
                        request.method = method_url[0]
                        request.url = method_url[1]
            else:
                return request
        else:
            return request
        

dryrun = False

try:
    options, args = getopt.getopt(sys.argv[1:], "hd", ["help", "dryrun"])
except getopt.GetoptError:
    print("python3 client-parser.py")
    sys.exit(2)
for option, arg in options:
    if option in ("-h", "--help"):
        print("python3 client-parser.py")
        sys.exit()
    elif option in ("-d", "--dryrun"):
        dryrun = True

with open("sample-http-client.http", "r") as file:
    reqs = []
    while (True):
        request = parse_request(file)
        if (request.name != ""):
            reqs.append(request)
            continue
        else:
            break
    print(dryrun)
    for request in reqs:
        print(request)
        if not dryrun:
            r = requests.get(url = request.url)
            data = r.json()
            print(data)