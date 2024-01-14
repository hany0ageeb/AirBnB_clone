#!/usr/bin/python3
"""This module define one class TestFileStorage
"""


import unittest
from io import StringIO
import json
from unittest.mock import patch
from random import random
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """tests for FileStorage class"""
    def test_class_attribute_file_path(self):
        """test FileStorage.__file_path exist"""
        self.assertTrue(
            hasattr(FileStorage, '_FileStorage__file_path'),
            msg="")

    def test_class_attribute_objects(self):
        """test FileStorage.__objects exist"""
        self.assertTrue(
            hasattr(FileStorage, '_FileStorage__objects'),
            msg="")

    def test_all_return__objects(self):
        """test return value of all"""
        objs = {}
        with patch(
                'models.engine.file_storage.FileStorage._FileStorage__objects',
                objs) as p:
            instance = FileStorage()
            self.assertEqual(instance.all(), objs)

    def test_new_add_obj_in_objects_if_not_exist(self):
        """test new method add the object to __objects if not exists in dict"""
        objs = {}
        with patch(
                'models.engine.file_storage.FileStorage._FileStorage__objects',
                objs) as p:
            instance = FileStorage()
            obj = BaseModel()
            obj.id = '123'
            instance.new(obj)
            self.assertTrue('BaseModel.123' in objs)
            self.assertEqual(obj, objs['BaseModel.123'])

    def test_new_set_obj_in_objects_if_exist(self):
        """test new method update object if exist in __objects"""
        obj = BaseModel()
        obj.id = '123'
        obj.first_name = 'hooo'
        objs = {
            'BaseModel.123': obj
        }
        with patch(
                'models.engine.file_storage.FileStorage._FileStorage__objects',
                objs) as p:
            instance = FileStorage()
            obj2 = BaseModel()
            obj2.id = '123'
            instance.new(obj2)
            self.assertEqual(obj2, objs['BaseModel.123'])
            self.assertIsNot(obj, objs['BaseModel.123'])

    def test_save(self):
        """test save method"""
        file_path = f"{int(random() * 1000)}.json"
        objects = {
            'BaseModel.12-12': BaseModel(id='12-12')
        }
        data = {
            'BaseModel.12-12': objects['BaseModel.12-12'].to_dict()
        }
        import os.path
        if os.path.exists(file_path):
            os.remove(file_path)
        with patch(
                (
                    'models.engine.file_storage.'
                    'FileStorage._FileStorage__file_path'),
                file_path):
            with patch((
                'models.engine.file_storage.'
                'FileStorage._FileStorage__objects'),
                    objects):
                instance = FileStorage()
                instance.save()
        file_data = None
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r') as f:
            file_data = json.load(f)
        self.assertEqual(data, file_data)
        os.remove(file_path)

    def test_reload_should_do_nothing_if_file_not_exist(self):
        """relaod should not raise exceptions if file does not exist"""
        file_path = f"{int(random() * 10000)}.json"
        import os.path
        if os.path.exists(file_path):
            os.remove(file_path)
        with patch((
            'models.engine.file_storage.'
            'FileStorage._FileStorage__file_path'),
                file_path):
            instance = FileStorage()
            instance.reload()

    def test_reload_should_load_data_from_file(self):
        """test reload should clear __objects and load it from file"""
        obj = BaseModel(id='123-123')
        data = {
            'BaseModel.123-123': obj.to_dict()
        }
        objects = {
        }
        file_path = f"file_{int(random() * 10000)}.json"
        with open(file_path, 'w') as fp:
            json.dump(data, fp)
        with patch(
                (
                    'models.engine.file_storage.'
                    'FileStorage._FileStorage__objects'
                ), objects):
            with patch(
                    (
                        'models.engine.file_storage.'
                        'FileStorage._FileStorage__file_path'), file_path):
                instance = FileStorage()
                instance.reload()
                self.assertTrue('BaseModel.123-123' in objects)
                self.assertEqual(objects['BaseModel.123-123'].id, '123-123')
        import os.path
        if os.path.exists(file_path):
            os.remove(file_path)
