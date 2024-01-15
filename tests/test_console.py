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

    def test_help_present(self):
        """Test help is present"""
        # setup
        instance = HBNBCommand()
        expected = (
                "\nDocumented commands (type help <topic>):\n"
                "========================================\n"
                "EOF  all  clear  count  create  destroy  "
                "help  quit  show  update\n\n")
        # execute
        with patch('sys.stdout', new=StringIO()) as f:
            instance.onecmd("help")
            self.assertEqual(f.getvalue(), expected)
