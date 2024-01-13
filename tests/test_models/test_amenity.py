#!/usr/bin/python3
"""This Module defines a"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """class TestAmenity to test Amenity class"""
    def test_attr_name_exist(self):
        """test Amenity name attribute exists"""
        obj = Amenity()
        self.assertTrue(
                hasattr(obj, 'name'),
                msg='amenity name attribute not here')

    def test_name_default_to_empty_str(self):
        """tests name attribute is defaulted to emppty string"""
        obj = Amenity()
        self.assertEqual(
                obj.name,
                '',
                msg='amenity name should be empty')

    def test_init_set_attributes_if_kwarg_present(self):
        """test init passes kwargs to super()"""
        obj = Amenity(name='xyz', id='123')
        self.assertEqual(obj.name, 'xyz', msg='name should be xyz')
        self.assertEqual(obj.id, '123', msg='id should be 123')
