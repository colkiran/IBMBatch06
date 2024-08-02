import json

import  requests

print("get".center(60, "-"))

BASE= "http://127.0.0.1:5000/"

response = requests.get(BASE + "getproduct/pepsi")

res = response.json()

for k,v in res.items():
    print(k, "=>", v)

print("put".center(60, "-"))

response = requests.put(BASE + "getproduct/coke", data={'cat': "baverage"})
res = response.json()

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)

print("patch".center(60,"-"))
data = {'price': 5000}
response = requests.patch(BASE + "getproduct/coke", json=json.dumps(data))
res = response.json()

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)

print("post".center(60, "-"))
fanta = {'item': '500 ml bottle', 'price': 60, 'qty' :300}

response = requests.post(BASE + "getproduct/fanta", json=json.dumps(fanta))
res = response.json()

for k, info in res.items():
    print(str(k).upper())
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)

print("delete".center(60, "-"))
response = requests.delete(BASE + "getproduct/thumbs")
res = response.json()

for k, info in res.items():
    print(str(k).upper())
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)

