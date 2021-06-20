import requests
import json

url = requests.get("https://api.androidhive.info/contacts/")

testData = url.text
print(testData)
print(type(testData))

data = json.loads(testData)
print(data)
print(type(data))

dic = data["contacts"][0]
print(dic['name'])
print(dic['email'])
print(dic['gender'])

print(data["contacts"][1])
persinInfo = data["contacts"][1]
print(persinInfo['name'])
print(persinInfo['email'])


