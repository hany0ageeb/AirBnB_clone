#!/usr/bin/python3
"""This module define one class TestFileStorage
"""


import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """class TestFileStorage defines FileStorage
    tests"""
    def test_attr_file_path_exist(self):
        """test FileStorage.__file_path exist"""
        self.assertTrue(
                hasattr(FileStorage, '_FileStorage__file_path'),
                msg='FileStorage.__file_path is not here!')

    def test_attr_objects_exist(self):
        """test FileStorage.__objects exist"""
        self.assertTrue(
                hasattr(FileStorage, '_FileStorage__objects'),
                msg='FileStorage.__objects is not here!')
