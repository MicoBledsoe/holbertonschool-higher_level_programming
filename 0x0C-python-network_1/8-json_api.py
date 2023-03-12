#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    response = requests.post(url, data=data)

    try:
        response_dict = response.json()
        if response_dict:
            print("[{}] {}".format(response_dict['id'], response_dict['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
