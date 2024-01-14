#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines a single class BaseModel
"""


import uuid
from datetime import datetime
from models.datetime_wrapper import get_now_datetime


class BaseModel:
    """Class BaseModel that defines all common attributes/methods
    for other classes
    Attributes:
        id (str):  assign with an uuid when an instance is created
        created_at (datetime): assign with the current
        datetime when an instance is created
        updated_at (datetime): assign with the current
        datetime when an instance is created
        and it will be updated every time you change your object
    """

    __storage = None

    def __init__(self, *args, **kwargs):
        self.__storage = None
        if not kwargs:
            self.id = str(uuid.uuid4())
            the_now = get_now_datetime()
            self.created_at = the_now
            self.updated_at = the_now
            BaseModel.getstorage().new(self)
        else:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    if type(value) is datetime:
                        self.__dict__[key] = value
                    else:
                        self.__dict__[key] = datetime.fromisoformat(value)
                elif key != '__class__' and key != 'id':
                    self.__dict__[key] = value
                elif key == 'id':
                    self.id = str(value)

    @classmethod
    def getstorage(cls):
        """read only property"""
        if BaseModel.__storage is None:
            from models import storage
            BaseModel.__storage = storage
        return BaseModel.__storage

    def __str__(self):
        """should return [<class name>] (<self.id>) <self.__dict__>
        """
        dictionary = {
                key: value
                for key, value in self.__dict__.items()
                if key != '_BaseModel__storage'
        }
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, dictionary)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = get_now_datetime()
        BaseModel.getstorage().save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        Returns:
            dict: containing all key/values of __dict__
        """
        ret_val = {}
        for key in self.__dict__.keys():
            if key not in ('created_at', 'updated_at'):
                if key != '_BaseModel__storage':
                    ret_val[key] = self.__dict__[key]
            else:
                ret_val[key] = self.__dict__[key].isoformat()
        ret_val['__class__'] = self.__class__.__name__
        return ret_val

    def addOrUpdate(self, **kwargs):
        """iterates over kwargs and update or add key/value"""
        if kwargs:
            for key, value in kwargs.items():
                if key not in self.__dict__:
                    self.__dict__[key] = value
                else:
                    if key in ('created_at', 'updated_at'):
                        if type(value) is datetime:
                            self.__dict__[key] = value
                        else:
                            self.__dict__[key] = datetime.fromisoformat(value)
                    elif key != '__class__':
                        self.__dict__[key] = type(self.__dict__[key])(value)
