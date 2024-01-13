#!/usr/bin/python3
"""This module defines a single class: Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class Review inherits from BaseModel"""

    place_id = ''
    user_id = ''
    text = ''
