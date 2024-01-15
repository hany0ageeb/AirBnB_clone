#!/usr/bin/python3
"""This module defines class TestConsole"""


import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """defines test cases for console"""

    def test_quit_present(self):
        """tests do_quit present"""
        # setup
        instance = HBNBCommand()
        # test
        self.assertTrue(hasattr(instance, 'do_quit'))
