import json

file1 = open("data.json","r")
data = json.load(file1)
print(type(data))

#loop in dict
for i in data:
    print(data[i])