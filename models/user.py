#!/usr/bin/python3
"""User module"""
import uuid
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from models.get_id_proyect import get_id_project
from models.get_project import get_project
from models.check_proyect_full import check_prj_full

Base = declarative_base()

class User(Base):
    """This class will defines all common attributes/methods
    for other classes
    """
    __tablename__ = "users"
    id = Column(String(60), primary_key=True, nullable=False)
    email = Column(String(60), nullable=False)
    api_key = Column(String(60), nullable=False)
    turns_ToDo = Column(Integer, default=0)
    turns_done = Column(Integer, default=0)
    points = Column(Integer, default=0)

    def __init__(self, email, api_key, auth_token, done=0):
        """Instantiation of base model class
        """
        self.id = str(uuid.uuid4())
        self.email = email
        self.api_key = api_key
        self.auth_token = auth_token
        self.done = done

    def set_token(self, token):
        self.auth_token = token

    def set_done(self, done=0):
        self.done = done

    def get_id_pj(self, password):
        """get_proyect_list | get code of proyects
        return: list of strings
        """
        self.prj_id = get_id_project(self.email, password)

    def get_project_task(self, proyect_id, token):
        """get_tasks | get id of tasks of proyects
        return: list of id tasks
        """
        return get_project(proyect_id, token)

    def all_checks(self, task_list, token):
        """all checks | get code of object corrections
        return: count of checks in true
        """
        return check_prj_full(task_list, token)


    def calc(self):
        """set to do and done
        """
        task_list = self.get_project_task(self.prj_id, self.auth_token)
        total_checks = self.all_checks(task_list, self.auth_token)
#        self.turns_done += self.done
        self.turns_ToDo = total_checks['done']
        return self.turns_ToDo - self.turns_done

    def save(self):
        """save | save a object user
        """
        models.storage.new(self)
        models.storage.save()
