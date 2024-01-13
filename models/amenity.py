#!/usr/bin/python3
"""This module defines a single class: Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        self.name = ''
        super().__init__(self, *args, **kwargs)
