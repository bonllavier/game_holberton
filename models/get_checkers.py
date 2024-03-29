#!/usr/bin/python3
""" Given a user's id_correction, ask for a correction of a task"""

import sys
import time


def get_checkers(id_correction, auth_token):
    """
    @id_correction: (int) correction id
    @auth_token: (int) user's auth_token

    returns: id of the correction made of that task
    """

    import requests
    import json

    if(id_correction is None or auth_token is None or int(id_correction) < 0):
        return None

    url = 'https://intranet.hbtn.io/correction_requests/'
    string = '.json?auth_token='
    dest_url = url + str(id_correction) + string + auth_token

    h = {
        'Content-Type': 'application/json',
    }
    checkers_dict = {}
    test = 1
    while test:
        time.sleep(5)
        url_response = requests.get(dest_url, h)
        checkers_dict = url_response.json()
        if 'Done' not in checkers_dict.get('status'):
            print("try again")
        else:
            test = 0

    if ('error' in checkers_dict):
        print('error checkers')
        checkers_dict = None
        return None

    results_list = []
    count = 0
    if 'result_display' in checkers_dict:
        results = checkers_dict.get('result_display')

        if 'checks' in results:
            results_list = results.get('checks')
            print(results_list)
            for i in results_list:
                if (i.get('passed') is True):
                    count = count + 1

    return (count, results_list)
