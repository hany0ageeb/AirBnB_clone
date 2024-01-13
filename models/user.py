#!/usr/bin/python3
"""This module defines on class: User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """class User inherits from BaseModel"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
