#!/usr/bin/python3
"""
 Python script that takes in a URL,
 sends a request to the URL and
 displays the body of the response (decoded in utf-8).
"""


import urllib.request
import urllib.error
from sys import argv

req = urllib.request.Request('argv[1]')
try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('UTF-8'))
except urllib.error.HTTPError as e:
    print(f'Error code: {e.code}')
