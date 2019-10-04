#!/usr/bin/python3
"""User module"""
import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

Base = declarative_base()

class User:
    """This class will defines all common attributes/methods
    for other classes
    """
    __tablename__ = "users"
    id = Column(String(60), primary_key=True, nullable=False)
    email = Column(String(128), nullable=False)


    def __init__(self, email, api_key, auth_token):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """

        self.id = str(uuid.uuid4())
        self.name = name
        self.auth_token = auth_token
