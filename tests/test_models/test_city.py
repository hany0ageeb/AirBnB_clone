#!/usr/bin/python3
"""this module defines a single class TestCity"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """class TestCity test City"""
    def test_state_id_attr_exist_and_empty_initially(self):
        """test state_id exist and initially empty"""
        self.assertTrue(
                hasattr(City, 'state_id'),
                msg='City.state_id is not here')
        self.assertEqual(
                City.state_id,
                '',
                msg='City.state_id should be initally empty')
        self.assertEqual(
                type(City.state_id),
                str,
                msg='City.state_id should be str')

    def test_name_attr_exist_and_not_empty_initially(self):
        """test name attr is exist and is empty string"""
        self.assertTrue(
                hasattr(City, 'name'),
                msg='City.name is not here')
        self.assertEqual(
                type(City.name),
                str,
                msg='City.name is not of str type')
        self.assertEqual(
                City.name,
                '',
                msg='City.name should be initially empty string')
