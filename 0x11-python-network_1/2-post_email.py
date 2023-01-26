#!/usr/bin/python3
"""
Python script that takes in a URL and an email, 
sends a POST request to the passed URL with the email as a parameter, 
and displays the body of the response (decoded in utf-8)
"""


import urllib.parse
import urllib.request
import sys

email = sys.argv[2]
url = sys.argv[1]
data = {'email': email}

data = urllib.parse.urlencode(data).encode()
with urllib.request.urlopen(url, data) as response:
    you_email = response.read().decode('utf-8')
    print(f"Your email is: {your_email}")