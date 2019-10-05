#!/usr/bin/python3
""" check all the task of a given proyect """

from models.get_correction import get_correction_id
from models.get_checkers import get_checkers


def check_prj_full(task_list, token):
    """ check all the proyects from a given task list
    and return a dictionary with the total task passed
    and the total task"""

    task = {
        'done': 0,
        'total': 0,
    }

    size = len(task_list)
    for i in range(size):
        correction_id = get_correction_id(task_list[i], token)
        print(i, correction_id, task_list[i])
        print("\n  Checkers: {:d}".format(i))
        checkers = get_checkers(correction_id, token)
        print(checkers)
        task['done'] += checkers[0]
        task['total'] += len(checkers[1])

    print(task)
    return(task)
