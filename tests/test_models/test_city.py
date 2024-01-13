#!/usr/bin/python3
"""this module defines a single class TestCity"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """class TestCity test City"""
    def test_state_id_attr_exist(self):
        """test state_id exist"""
        obj = City()
        self.assertTrue(
                hasattr(obj, 'state_id'),
                msg='state_id does not exist')

    def test_state_id_default_empty_str(self):
        """test state_id defaults to empty string"""
        obj = City()
        self.assertEqual(
                obj.state_id,
                '',
                msg="state_id should be initially empty")

    def test_name_attr_exist(self):
        """test city name attribute exist"""
        obj = City()
        self.assertTrue(
                hasattr(obj, 'name'),
                msg='name does not exist')

    def test_name_initially_empy(self):
        """test city name initially empty string"""
        obj = City()
        self.assertEqual(obj.name, '', msg="city name should be empy")

    def test_init_calling_BaseModel_init(self):
        """test city.__init__ passing kwargs to BaseModel.__init__"""
        obj = City(name='new york', state_id='123-123')
        self.assertEqual(
                obj.name,
                'new york',
                msg='city name should be new york')
        self.assertEqual(obj.state_id, '123-123', msg='city state_id not set')
