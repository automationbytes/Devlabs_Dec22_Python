import requests
import json
import jsonpath
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

req = requests.delete("http://webservice.toscacloud.com/rest/api/Shops_V2/67614")
print(req.status_code)


req = requests.get("http://webservice.toscacloud.com/rest/api/Shops_V2")
print(req.status_code)
print(json.dumps(req.json(),indent=4))


