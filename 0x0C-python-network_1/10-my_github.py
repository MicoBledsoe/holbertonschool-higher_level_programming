#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    response = requests.get(url, auth=(username, token))
    if response.status_code != 200:
        print("Error: Could not get user information")
    else:
        print(response.json()['id'])
