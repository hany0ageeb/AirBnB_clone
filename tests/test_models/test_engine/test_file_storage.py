#!/usr/bin/python3
"""This module define one class TestFileStorage
"""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


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

    def test_all_exist(self):
        """test all instance method exist"""
        obj = FileStorage()
        self.assertTrue(
                hasattr(obj, 'all'),
                msg='instance method all does not exist!')

    def test_all_returns__object(self):
        """check all returns __objects dictionary"""
        obj = FileStorage()
        self.assertEqual(
                FileStorage._FileStorage__objects,
                obj.all(),
                msg='all should return __objects')

    def test_new_add_or_update_obj_in_objects(self):
        """test new(self, obj): sets in __objects
        the obj with key <obj class name>.id"""
        storage = FileStorage()
        obj = BaseModel()
        obj.id = '123-123'
        storage.new(obj)
        self.assertTrue(
                'BaseModel.123-123' in FileStorage._FileStorage__objects,
                msg='new did not add obj to __objects')
