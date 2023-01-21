import requests
import json
import jsonpath
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

myobj = {
  "Address": {
    "City": "Chennai",
    "Country": "India",
    "Street": "Camp Road",
    "ZipCode": 600007
  },
  "FirstName": "Tom",
  "Id": 4,
  "LastName": "Jerry"
}


req = requests.put("http://webservice.toscacloud.com/rest/api/Employee_V2")
print(req.status_code)

print(json.dumps(req.json(),indent=4))

req = requests.get("http://webservice.toscacloud.com/rest/api/Employee_V2")
print(req.status_code)
print(json.dumps(req.json(),indent=4))



