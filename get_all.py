#!/usr/bin/python3
""" collects all the info"""

from models.get_token import get_token
from models.get_profile import get_profile
from models.get_project import get_project
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

print("\n  Tasks: **********************")
task_list = get_project(270, token)
print(task_list)

print("\n  Correction id: ********************")
correction_id = get_correction_id(task_list[14], token)
print(correction_id)

print("\n  Checkers: **********************")
checkers_list = get_checkers(correction_id, token)
print(checkers_list)