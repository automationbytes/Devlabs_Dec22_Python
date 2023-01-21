import requests
import json
import jsonpath
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

myobj = {
  "City": "Delhi",
  "Country": "India",
"Id": 67615,
  "Name": "Hi"
}
req = requests.put("http://webservice.toscacloud.com/rest/api/Shops_V2",json=myobj)
print(req.status_code)

print(json.dumps(req.json(),indent=4))

req = requests.get("http://webservice.toscacloud.com/rest/api/Shops_V2")
print(req.status_code)
print(json.dumps(req.json(),indent=4))



