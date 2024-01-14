#!/usr/bin/python3
"""This Module defines a"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """class TestAmenity to test Amenity class"""
    def test_name_attr_exist(self):
        """test class attribute name exist"""
        self.assertTrue(
                hasattr(Amenity, 'name'),
                msg='Amenity.name is not here!')

    def test_name_attr_is_str(self):
        """test class attribute name is of type str"""
        self.assertEqual(
                type(Amenity.name),
                str,
                msg='Amenity.name should be of type str!')
