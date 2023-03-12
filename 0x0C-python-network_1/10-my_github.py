#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    access_token = sys.argv[2]
    url = f'https://api.github.com/user'
    response = requests.get(url, auth=(username, access_token))
    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print("Error: Could not get user information")
        print(response.text)
        sys.exit(1)
