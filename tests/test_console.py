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

    def test_emptyline_present(self):
        """Test empty line is present"""
        instance = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as f:
            with patch.object(instance, 'emptyline') as empt:
                instance.onecmd("\n")
            empt.assert_called_once()
            self.assertEqual(f.getvalue(), '')

    def test_create_BaseModel_should_print_class_name_missing(self):
        """Test create BaseModel is present"""
        instance = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as f:
            instance.onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_create_BaseModel_should_print_class_doesnot_exist(self):
        """Test create BaseModel =is present"""
        instance = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as f:
            instance.onecmd("create plapla")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_create_BaseModel_should_print_id(self):
        """Test create BaseModel"""
        with patch('builtins.open', return_value=StringIO()):
            with patch('uuid.uuid4', return_value='123-123'):
                instance = HBNBCommand()
                with patch('sys.stdout', new=StringIO()) as f:
                    instance.onecmd("create BaseModel")
                    self.assertEqual(f.getvalue(), '123-123\n')
