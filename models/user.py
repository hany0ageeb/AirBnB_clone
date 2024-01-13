#!/usr/bin/python3
"""This module defines on class: User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """class User inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
        super().__init__(self, *args, **kwargs)
