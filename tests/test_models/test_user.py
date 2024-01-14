#!/usr/bin/python3
"""this module defines a single class: TestUser"""


import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """defines tests for class User"""
    def test_email_exist(self):
        """tests email class attribute exist"""
        self.assertTrue(hasattr(User, 'email'))

    def test_email_is_str(self):
        """test email attribute is string"""
        self.assertTrue(type(User.email) is str)

    def test_password_attribute_exist(self):
        """tests class attribute password exist"""
        self.assertTrue(hasattr(User, 'password'))

    def test_password_is_str(self):
        """test class atrribute str is of type str"""
        self.assertTrue(type(User.password) is str)

    def test_first_name_exist(self):
        """test class attribute first_name exist"""
        self.assertTrue(hasattr(User, 'first_name'))

    def test_first_name_is_str(self):
        """test class attribute first_name is str"""
        self.assertTrue(type(User.first_name) is str)

    def test_last_name_exist(self):
        """tests class attribute last_name exist"""
        self.assertTrue(hasattr(User, 'last_name'))

    def test_last_name_is_str(self):
        """tests class attribute last_name if str"""
        self.assertTrue(type(User.last_name) is str)
