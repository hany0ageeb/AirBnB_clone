#!/usr/bin/python3
"""This module defines a single class TestBaseModel"""


import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestBaseModel tests BaseModel"""

    def test_id_exist_if_no_kwargs(self):
        """tests __init__ create id attribute if no kwargs is given"""
        obj = BaseModel()
        self.assertTrue(
                hasattr(obj, 'id'),
                msg=f'BaseModel object lacks id attribute')

    def test_init_id_is_given_value_using_uuid4_no_kwargs(self):
        """test __init__ assign id a value using uuid4 if not given kwargs"""
        with patch('uuid.uuid4', return_value='123-123') as p:
            obj = BaseModel()
        p.assert_called()
        self.assertEqual(obj.id, '123-123', msg='obj.id is not set to 123-123')

    def test_init_created_at_exist_if_no_kwargs(self):
        """test __init__ cretae created_at attribute if no kwargs is given"""
        obj = BaseModel()
        self.assertTrue(
                hasattr(obj, 'created_at'),
                msg="no created_at attribute")

    def test_init_updated_at_exist_if_no_kwags(self):
        """test __iit__ create update_at attribute if no kwargs is given"""
        obj = BaseModel()
        self.assertTrue(
                hasattr(obj, 'updated_at'),
                msg="cannt find updated_at")

    def test_init_with_kwargs_should_ignore__class__(self):
        kwargs = {'id': '123-123', '__class__': 'plapla'}
        obj = BaseModel(**kwargs)
        self.assertNotEqual(
                obj.__class__,
                'plapla',
                msg="should ignore __class__ in kwargs")

    def test_init_raise_value_error_if_created_at_not_isoformat(self):
        kwargs = {'id': '123-123', 'created_at': 'popopopo'}
        with self.assertRaises(ValueError):
            obj = BaseModel(**kwargs)

    def test_init_change_attributes_if_present_in_kwargs(self):
        created_a = datetime.now().isoformat()
        updated_a = datetime.now().isoformat()
        kwargs = {
                'id': '123',
                'created_at': created_a,
                'updated_at': updated_a}
        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, '123', msg='__init did not set id attribute!')
        self.assertEqual(
                obj.created_at,
                datetime.fromisoformat(created_a),
                msg='__init did not set created_at!')
        self.assertEqual(
                obj.updated_at,
                datetime.fromisoformat(updated_a),
                msg='__init did not set updated_at!')

    def test_to_dict_exists(self):
        """tests the existence of to_dict method"""
        obj = BaseModel()
        ret = hasattr(obj, 'to_dict')
        self.assertTrue(ret, 'BaseModel has no to_dict present.')

    def test_to_dict_return_dictionary(self):
        """test that to_dict return a dictionary"""
        obj = BaseModel()
        ret = obj.to_dict()
        self.assertIsInstance(
                ret,
                dict,
                'to_dict return value is not a dictionary.')

    def test_to_dict_return_value(self):
        """test return value of to_dict method"""
        created_a = datetime(2024, 12, 31)
        updated_a = datetime(2024, 1, 13)
        expected = {
                'id': '123-123',
                'created_at': created_a.isoformat(),
                'updated_at': updated_a.isoformat(),
                '__class__': 'BaseModel'
        }
        obj = BaseModel()
        obj.id = '123-123'
        obj.created_at = created_a
        obj.updated_at = updated_a
        result = obj.to_dict()
        self.assertEqual(
                result,
                expected,
                msg='to_dict method return a valid result.')

    def test_addOrUpdate_change_existing_attr_value(self):
        """test calling saveOrUpdate change existing attribute value"""
        obj = BaseModel()
        new_id = '123-123'
        obj.addOrUpdate(id=new_id)
        self.assertEqual(
                obj.id,
                new_id,
                msg='addorUpdate did not change id attribute')

    def test_addOrUpdate_add_attr_if_not_exist(self):
        obj = BaseModel()
        if hasattr(obj, 'first_name'):
            del obj.first_name
        obj.addOrUpdate(first_name='hany')
        self.assertTrue(
                hasattr(obj, 'first_name'),
                msg='first_name does not exist')
        self.assertEqual(obj.first_name, 'hany', 'first_name not equal hany')

    def test_addOrUpdate_raise_valueError_when_given_invalid_datetime(self):
        """test addOrUpdate raise ValueError"""
        obj = BaseModel()
        with self.assertRaises(ValueError):
            obj.addOrUpdate(updated_at='invalid date iso format')

    def test_addOrUpdate_cast_value(self):
        """test addOrUpdate cast value before update existing attribute"""
        obj = BaseModel()
        obj.addOrUpdate(id=123)
        self.assertIsInstance(
                obj.id,
                str,
                msg='addOrUpdate did not cast int to str for id')

    def test_str_return_value(self):
        """test BaseModel str return Value"""
        obj = BaseModel()
        result = str(obj)
        expected = f'[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}'
        self.assertEqual(result, expected)
