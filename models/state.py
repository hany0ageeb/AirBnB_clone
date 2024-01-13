#!/usr/bin/python3
"""This module defines a single class: State
"""

from models.base_model import BaseModel


class State(BaseModel):
    """class State inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        self.name = ''
        super().__init__(self, *args, **kwargs)
