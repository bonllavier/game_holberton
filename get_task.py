#!/usr/bin/python3
""" Given a user's id_task, returns the json_file of that task"""

import sys


def get_task(id_task, auth_token):
    """
    @id_task: (int) task id
    @auth_token: (int) user's auth_token

    returns: None if no checkers available, or json file otherwise
    """

    import requests

    if(id_task is None or auth_token is None or int(id_task) < 0):
        return []

    url = 'https://intranet.hbtn.io/tasks/'

    dest_url = url + str(id_task) + '.json?auth_token=' + auth_token

    h = {
        'Content-Type': 'application/json',
    }

    url_response = requests.get(dest_url, h)
    task_json = url_response.json()

    if ('error' in task_json):
        print('error task')
        task_json = None
        return None
    print(task_json)
    return (task_json)

get_task(sys.argv[1], sys.argv[2])
