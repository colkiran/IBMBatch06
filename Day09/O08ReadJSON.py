
# load is used to read the Json document from a file
# loads is used to covert JSON string to python dictionary

import json

JFR = open("books.json", "r")
jsonFile = json.load(JFR)

# print(jsonFile)
for book in jsonFile['books']:
    print(book['name'])
    print("-" * len(book['name']))
    for k, v in book.items():
        print(k, "=>", v)
    print("-" * 60)