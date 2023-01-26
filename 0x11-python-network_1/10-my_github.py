#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
from sys import argv

url = 'https://api.github.com/user'
username = argv[1]
pat = argv[2]

r = requests.get(url, auth=(username, pat))
data = r.json().get("id")
print(data)
