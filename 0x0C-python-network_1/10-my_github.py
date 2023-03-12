#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == '__main__':
    # Get the command line arguments
    username, password = sys.argv[1:]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    # Check the response status code
    if response.status_code != 200:
        print("Error: Could not get user information")
        sys.exit(1)

    # Print the user id
    print(response.json()['id'])
