#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import User

# creation of a State
myUser = User("785@holbertonschool.com", "a5b011fcc91091b2c45e1e6348d892e2", "2995a219f61d91010f48a42a9012523d298577a75eeea97165427ecbdb1517b5")
#print(type(myUser))
#print(dir(myUser))
myUser.save()
print(myUser.points)
print("OK")
