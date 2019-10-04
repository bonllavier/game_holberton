#!/usr/bin/python3
""" Given user ID, returns information about his/her TODO list progress"""

import sys


def get_token(email, password, api_key):
    """
    @email: User's email .
    @password: user's password.
    api_key: user's api key
    """

    import requests

    if(email is None or password is None or api_key is None):
        return None

    if(len(email) == 1 or len(password) == 1 or len(api_key) == 1):
        return None

    if(type(api_key) == 'str' and not(api_key.find('@'))):
        return None

    url = 'https://intranet.hbtn.io/users/auth_token.json'
    h = {
        'Content-Type': 'application/json',
    }

    d = {"api_key": api_key, "email": email, "password": password,
         "scope": 'checker'}

    url_response = requests.post(url, d)
    auto_token = url_response.json().get('auth_token')
    print(auto_token)

get_token(sys.argv[1], sys.argv[2], sys.argv[3])
