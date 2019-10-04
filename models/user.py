#!/usr/bin/python3
"""User module"""
import uuid
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    """This class will defines all common attributes/methods
    for other classes
    """
    __tablename__ = "users"
    id = Column(String(60), primary_key=True, nullable=False)
    email = Column(String(60), nullable=False)
    api_key = Column(String(60), nullable=False)
    auth_token = Column(String(128), nullable=False)
    tries = Column(Integer, default=0)


    def __init__(self, email, api_key, auth_token):
        """Instantiation of base model class
        """
        self.id = str(uuid.uuid4())
        self.email = email
        self.api_key = api_key
        self.auth_token = auth_token

    def get_proyect_list(self, password):
        """get_proyect_list | get code of proyects
        return: list of strings
        """
        pass

    def get_tasks(self, proyect_id=None):
        """get_tasks | get id of tasks of proyects
        return: list of id tasks
        """
        pass
    def get_start_correction(self):
        """get_start correction | get code of object corrections
        return: list of id start correction
        """
        pass

    def all_checks(self):
        """all checks | get code of object corrections
        return: count of checks in true
        """
        pass

    def set_tries(self):
        """set tries | set a property tries
        """
        pass

    def save(self):
        """save | save a object user
        """
        models.storage.new(self)
        models.storage.save()
