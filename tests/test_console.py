#!/usr/bin/python3
"""This module defines class TestConsole"""


import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """defines test cases for console"""

    def test_quit_present(self):
        """tests do_quit present"""
        # setup
        instance = HBNBCommand()
        with self.assertRaises(SystemExit):
            instance.onecmd("quit")

    def test_EOF_present(self):
        """test EOF exist"""
        # setup
        instance = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as f:
            instance.onecmd('EOF')
        self.assertEqual(f.getvalue(), '\n')
