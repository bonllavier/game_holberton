#!/usr/bin/python3
""" Given a user's id_task, returns the correction id made on that task"""

import sys
import time


def get_correction_id(id_task, auth_token):
    """
    @id_task: (int) task id
    @auth_token: (int) user's auth_token

    returns: id of the correction made of that task
    """

    import requests

    if(id_task is None or auth_token is None or int(id_task) < 0):
        return None

    url = 'https://intranet.hbtn.io/tasks/'
    string = '/start_correction.json?auth_token='
    dest_url = url + str(id_task) + string + auth_token

    h = {
        'Content-Type': 'application/json',
    }

    d = (
        ('auth_token', auth_token),
    )

    url_response = requests.post(dest_url, h, d)
    correction_json = url_response.json()

    if ('error' in correction_json):
        print(correction_json.get('error'))
        correction_json = None
        return None
    return (correction_json.get('id'))
