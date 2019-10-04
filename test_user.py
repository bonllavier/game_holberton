#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import User

# creation of a State
myUser = User("myemail", "mypass", "myauth")
print(type(myUser))
print(dir(myUser))
myUser.save()

print("OK")
