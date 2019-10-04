#!/usr/bin/python3
""" Given user email, password and api_key returns the api_token"""

import sys


def get_token(email, password, api_key):
    """
    @email: User's email .
    @password: user's password.
    api_key: user's api key

    returns: None is a parameter is invalid or the user's api token
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
    auth_token_json = url_response.json()

    if ('error' in auth_token_json):
        print('error token')
        auth_token = None

    auth_token = auth_token_json.get('auth_token')

    return (auth_token)
