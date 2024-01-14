#!/usr/bin/python3
"""This module defines a single class: TestState"""

from models.state import State
import unittest


class TestState(unittest.TestCase):
    """defines tests cases for class State"""
    def test_name_exist(self):
        """test name attribute exist"""
        self.assertTrue(
                hasattr(State, 'name'),
                msg='State.name is not here!')

    def test_name_of_type_str(self):
        """test name attribute is of type str"""
        self.assertEqual(
                type(State.name),
                str,
                msg='State.name should be of type str')
