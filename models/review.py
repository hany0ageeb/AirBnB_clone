#!/usr/bin/python3
"""This module defines a single class: Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class Review inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        self.place_id = ''
        self.user_id = ''
        self.text = ''
        super().__init__(self, *args, **kwargs)
