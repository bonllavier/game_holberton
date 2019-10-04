#!/usr/bin/python3
""" Given a user's id_proiect, returns a task list of the project"""

import sys


def get_project(id_project, auth_token):
    """
    @id_project: (int) project id
    @auth_token: (int) user's auth_token

    returns: list of all id tasks of the project or None
    """

    import requests

    if(id_project is None or auth_token is None or int(id_project) < 0):
        return []

    url = 'https://intranet.hbtn.io/projects/'

    dest_url = url + str(id_project) + '.json?auth_token=' + auth_token

    h = {
        'Content-Type': 'application/json',
    }

    url_response = requests.get(dest_url, h)
    project_json = url_response.json()

    if ('error' in project_json):
        print('error project')
        project_json = None
        return []
    dict_tasks = (project_json.get('tasks'))
    task_list = []
    for task in dict_tasks:
        task_list.append(task['id'])

    return (task_list)
