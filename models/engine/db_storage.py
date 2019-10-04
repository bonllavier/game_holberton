#!/usr/bin/python3
"""This is the file DBStorage class for AirBnB"""
import json
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.user import User, Base

type_class = ["User"]


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __engine = None
    __session = None

    def __init__(self):
        """method constructor of objects DBStorage
        Return:
            Nothing
        """

        s = 'mysql+mysqldb://{}:{}@{}/{}'.format("app_dev",
                                                 "app_dev_pwd",
                                                 "0.0.0.0",
                                                 "app_dev_db")
        self.__engine = create_engine(s, pool_pre_ping=True)


    def get_user(self, id):
        """close the session
        Return: Nothing
        """
        user = self.__session.query(User).filter(User.id == id).one_or_none()
        return(user)

    def check_user(self, email):
        """close the session
        Return: Nothing
        """
        check = self.__session.query(User).filter(User.email == email).one_or_none()
        return(check)

    def close(self):
        """close the session
        Return: Nothing
        """
        self.__session.close()

    def new(self, obj):
        """add the object to the current database session
        Args:
            obj: given object
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None
        Return:
            Nothing
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and create the current database
        session
        """
        Base.metadata.create_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
