import requests
import json
import jsonpath
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

req = requests.get("http://webservice.toscacloud.com/rest/api/Employee_V2",headers={'Authorization': '37b836e4-6aaa-4cf8-8690-bb4b2a6be41c'})
print(req.status_code)
# print(req.text)
#print(req.json())
print(json.dumps(req.json(),indent=4))
json_Data = json.loads(req.text)


# for record in req.json():
#    print(record["FirstName"])

# with open('./movies.json') as movies_json:
# 	movies = json.load(movies_json)
# #json_exp = parse("$.movies[?(@.cast[:] =~ 'De Niro')].title")
# jsonpath_expression = parse("$.movies[?(@.title == 'Mean Streets')]")
#firstname = jsonpath_expression.find(movies)

json_exp = parse('$[?(@.FirstName == "Edward")].Address')
firstname = json_exp.find(json_Data)
print(firstname)
print("********")
print(firstname[0].value)
# for f in firstname:
#     print(f.value)