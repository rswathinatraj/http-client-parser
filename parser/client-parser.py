import re
import RequestFactory, HttpRequest
import sys, getopt
import json

def extract_name(line):
    name = re.search(r"([#]{3}) ([a-zA-Z]*)", line)
    return name.group(2)

def extract_method_url(line):
    method_url = re.search(r"([GET|POST|DELETE|PUT]+) (.*)", line)
    return method_url.groups()
        

def parse_request(file):
    request = HttpRequest.Request()
    request_factory = RequestFactory.Factory()
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
                request_factory.request = request
                return request_factory.construct_request()
        else:
            if (request.name):
                request_factory.request = request
                return request_factory.construct_request()   
            else:
                return
        
def main():
    dryrun:bool = False
    env:str = ""
    env_vars = {}

    try:
        options, args = getopt.getopt(sys.argv[1:], "hde:", ["help", "dryrun", "env="])
    except getopt.GetoptError:
        print("python3 client-parser.py")
        sys.exit(2)
    for option, arg in options:
        if option in ("-h", "--help"):
            print("python3 client-parser.py")
            sys.exit()
        elif option in ("-d", "--dryrun"):
            dryrun = True
        elif option in ("-e", "--env"):
            env = arg     

    if env != "":
        with open("http-client.env.json", "r") as file:
            data = json.loads(file.read())
            env_vars = data.get(env)

    with open("sample-http-client.http", "r") as file:
        reqs:HttpRequest.Request = []
        while (True):
            request = parse_request(file)
            if (isinstance(request, HttpRequest.Request) and request.name != ""):
                reqs.append(request)
                continue
            else:
                break
        for request in reqs:
            if not dryrun:
                request.replace_env_vars(env_vars)
                data = request.call_request()
                print(data)

main()