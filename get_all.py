#!/usr/bin/python3
""" collects all the info"""

from models.get_token import get_token
from models.get_profile import get_profile
from models.get_project import get_project
from models.get_id_proyect import get_id_project
from models.get_correction import get_correction_id
from models.get_checkers import get_checkers


import sys

token = get_token(sys.argv[1], sys.argv[2], sys.argv[3])
print("\n  Token: ************************")
print(token)
if (token is not None):
    email = sys.argv[1]
    password = sys.argv[2]
    api_key = sys.argv[3]

print("\n  User: **********************")
user = get_profile(token)
print(user)


print("\n  Proyects: **********************")
projects_dict = get_id_project(email, password)
print(projects_dict)


print("\n  Tasks: **********************")
task_list = get_project(300, token)
print(task_list)

print("\n  Correction id: ********************")
size = task_list.__len__

for (i = 0; i < size; i++):
    correction_id = get_correction_id(task_list[i], token)
    print(i, correction_id, task_list[correction_id])

print("\n  Checkers: **********************")
checkers_list = get_checkers(correction_id, token)
print(checkers_list)