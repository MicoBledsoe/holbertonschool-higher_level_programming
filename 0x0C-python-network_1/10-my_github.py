#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == '__main__':
    # Get the command line arguments
    if len(sys.argv) != 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)
    username = sys.argv[1]
    token = sys.argv[2]

    # Set up the request headers with Basic Authentication
    url = 'https://api.github.com/user'
    headers = {'Authorization': 'Basic ' + username + ':' + token}

    # Send the GET request
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code != 200:
        print("Error: Could not get user information")
        sys.exit(1)

    # Print the user id
    print(response.json()['id'])
