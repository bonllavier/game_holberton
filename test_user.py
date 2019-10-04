#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import User

# creation of a State
myUser = User("754@holbertonschool.com", "zbY%PY8ZES3g", "82c6b8c671ff62f1010fe8cbb1ed727c")
print(type(myUser))
print(dir(myUser))
myUser.save()

print("OK")
