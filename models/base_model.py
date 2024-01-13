#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines a single class BaseModel
"""


import uuid
from datetime import datetime
from models import storage


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
    def __init__(self, *args, **kwargs):
        if not kwargs:
            # from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
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

    def __str__(self):
        """should return [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        # from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        Returns:
            dict: containing all key/values of __dict__
        """
        ret_val = {}
        for key in self.__dict__.keys():
            if key not in ('created_at', 'updated_at'):
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
