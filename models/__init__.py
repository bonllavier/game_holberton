#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.user import User

"""
storage = DBStorage()
storage.reload()
"""