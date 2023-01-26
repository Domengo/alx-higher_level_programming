#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
- Display Not a valid JSON if the JSON is invalid
- Display No result if the JSON is empty
"""
import sys
import requests

q = "" if len(sys.argv) < 2 else sys.argv[1]

url = "http://0.0.0.0:5000/search_user"
response = requests.post(url, json={'q': q})

try:
    data = response.json()
except ValueError:
    print("Not a valid JSON")
    sys.exit(1)

if not data:
    print("No result")
    sys.exit(1)

for user in data:
    print("[{}] {}".format(user['id'], user['name']))
