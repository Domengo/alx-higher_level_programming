#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge.
- The first argument will be the repository name
- The second argument will be the owner name
- You must use the packages requests and sys
- You are not allowed to import packages other than requests and sys
- You don’t need to check arguments passed to the script (number or type)
"""

import requests
from sys import argv

OWNER = argv[2]
REPO = argv[1]

url = f'https://api.github.com/repos/{OWNER}/{REPO}/commits'

r = requests.get(url)
data = r.json()

author = data[0]["commit"]["author"]
name = author["name"]
print(f'{data[0]["sha"]}: {name}')
