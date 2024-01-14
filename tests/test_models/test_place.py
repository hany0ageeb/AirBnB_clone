#!/usr/bin/python3
"""This module defines a single class TestPlace"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """class TestPlace test Place class"""
    def test_city_id_exist(self):
        """test city_id attribute exist"""
        obj = Place()
        self.assertTrue(
                hasattr(obj, 'city_id'),
                msg='city state_id attr is not here!')

    def test_city_id_initially_empty(self):
        """test city_id is initially empty string"""
        obj = Place()
        self.assertEqual(
                obj.city_id,
                '',
                msg='city state_id is not empty str')

    def test_init_set_city_id(self):
        """test city_id is set if present in __init__"""
        obj = Place(city_id='123-123')
        self.assertEqual(
                obj.city_id,
                '123-123',
                msg="state_id should be 123-123")

    def test_user_id_exist(self):
        """test user_id attribute exist"""
        obj = Place()
        self.assertTrue(
                hasattr(obj, 'user_id'),
                msg='Place user_id does not exist')

    def test_user_id_initially_empty(self):
        """test user_id attribute initially empt"""
        obj = Place()
        self.assertEqual(obj.user_id, '', msg='uer_id is not empty')

    def test_init_set_user_id(self):
        """test init setting usr_id if given"""
        obj = Place(user_id='123-123')
        self.assertEqual(obj.user_id, '123-123', msg='user_id is not set')

    def test_name_attr_exist(self):
        """test name attribute exist"""
        obj = Place()
        self.assertTrue(
                hasattr(obj, 'name'),
                msg='place name attribute does not exit')

    def test_name_attr_initially_empty(self):
        """test name is set to empty str initially"""
        obj = Place()
        self.assertEqual(
                obj.name,
                '',
                msg='name atribute is not empty initially')

    def test_init_set_name_attr(self):
        """test name attribute is set to the passed value"""
        obj = Place(name='pla')
        self.assertEqual(
                obj.name,
                'pla',
                msg='name is not set to passed value')

    def test_description_attr_exist(self):
        """test description attribute exist"""
        obj = Place()
        self.assertTrue(
                hasattr(obj, 'description'),
                msg='description attribute does not exist')

    def test_description_initially_empty(self):
        """test description is initially empty string"""
        obj = Place()
        self.assertEqual(
                obj.description,
                '',
                msg='descriuption should be empty string')

    def test_init_set_description_attr(self):
        """test __init__ set description"""
        obj = Place(description='desc')
        self.assertEqual(
                obj.description,
                'desc',
                msg='__init did not set descriptiuon')

    def test_number_rooms_initially_zero(self):
        """test number_rooms is initially zero"""
        pass
