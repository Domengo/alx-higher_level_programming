#!/bin/bash

# check if a URL is provided as an argument
if [ -z "$1" ]; then
  echo "Please provide a URL as an argument"
  exit 1
fi

# send a GET request to the URL and store the response in a variable
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# check if the response status code is 200
if [ "$response" -eq 200 ]; then
  # display the body of the response
  curl -s "$1"
else
  echo "Error: Response status code is not 200"
fi
