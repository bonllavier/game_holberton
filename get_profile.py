#!/usr/bin/python3
""" Given user auth_token, returns information about the user profile"""

import sys


def get_profile(auth_token):
    """
    @auth_token: authorization token of a single user

    returns: json file with user's profile or None if error
    """

    import requests

    if(auth_token is None):
        return None

    url = 'https://intranet.hbtn.io/users/me.json?auth_token='
    dest_url = url + str(auth_token)

    h = {
        'Content-Type': 'application/json',
    }

    url_response = requests.get(dest_url, h)
    user_json = url_response.json()

    if ('error' in user_json):
        print('error profile')
        user_json = None
        return None
    print(user_json)
    return (user_json)

get_profile(sys.argv[1])
