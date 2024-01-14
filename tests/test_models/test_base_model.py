#!/usr/bin/python3
"""This module defines a single class TestBaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """TestBaseModel tests BaseModel"""

    def test_id_attribute_assign_default_value(self):
        """test id attribute is defaulted to uuid4() function"""
        with patch('uuid.uuid4', return_value='123-123') as p:
            instance = BaseModel()
            p.assert_called_once()
            self.assertEqual(instance.id, '123-123')

    def test_created_at_attribute_exist(self):
        """test created_at attribute defults to now"""
        the_now = datetime(2024, 1, 1)
        with patch('models.base_model.get_now_datetime',
                   return_value=the_now) as p:
            instance = BaseModel()
            self.assertEqual(
                    instance.created_at,
                    the_now,
                    msg='created_at should be assigned now()')
            p.assert_called_once()

    def test_str_return_value(self):
        """test return value of __str__ method"""
        # setup
        instance = BaseModel()
        instance.id = '1233'
        dictionary = {
                'id': instance.id,
                'created_at': datetime(2024, 1, 1),
                'updated_at': datetime(2024, 1, 12)
        }
        expected = f'[BaseModel] (1233) {dictionary}'
        # execute
        with patch.object(instance, '__dict__', new=dictionary) as p:
            result = str(instance)
            # test
            self.assertEqual(
                result,
                expected,
                msg=f"__str__ returns: \n{result}\nwhich is not right")

    def test_to_dict(self):
        """test return value of to_dict method"""
        # setup
        instance = BaseModel()
        instance.id = '123'
        d1 = datetime(2024, 1, 1)
        d2 = datetime(2024, 1, 2)
        instance.created_at = d1
        instance.updated_at = d2
        expected = {
                'id': '123',
                'created_at': d1.isoformat(),
                'updated_at': d2.isoformat(),
                '__class__': 'BaseModel'
        }
        # execute
        result = instance.to_dict()
        # test
        self.assertEqual(
                result,
                expected,
                msg=f'to_dict returns wrong value!')

    def test_save_updates_updated_at_atribute(self):
        """test save method udates updated_at attribute"""
        the_now = datetime(2024, 1, 1)
        instance = BaseModel()
        with patch('models.base_model.get_now_datetime',
                   return_value=the_now) as p:
            # execute
            instance.save()
            # test
            p.assert_called_once()
            self.assertEqual(
                    instance.updated_at,
                    the_now,
                    "save should update updated_at attribute.")

    def test_init_from_kwargs(self):
        """test the kwargs in __init add attribute to instance"""
        # setup
        instance = BaseModel(first_name='hooon')
        # test
        self.assertTrue(
                hasattr(instance, 'first_name'),
                msg="__init(first_name='hooo') is ignored first_name=hooon")

    def test_init_set_id_from_kwargs_and_do_not_call_uuid4(self):
        """test id is set from kwargs and uuid4() is not called"""
        with patch('uuid.uuid4', return_value='1-2') as p:
            instance = BaseModel(id='pla')
            self.assertEqual(
                    instance.id,
                    'pla',
                    msg="__init(id=pla) did not set id attribute")
            p.assert_not_called()

    def test_init_set_created_at_from_isoformatdatetime(self):
        """test creatd_at is set from a isodattimeformat
        string which get converted to datetime"""
        created_at = datetime(2024, 1, 1)
        instance = BaseModel(created_at=created_at.isoformat())
        self.assertEqual(created_at, instance.created_at)

    def test_init_raise_valueerror_when_creaetd_at_isnot_isoformat(self):
        """test __init raises ValueError when created_at
        string is not of isoformat"""
        c_at = 'invalid isoformat dattime string'
        with self.assertRaises(ValueError):
            BaseModel(created_at=c_at)

    def test_init_uodated_at_is_set(self):
        """test if updated_at attribute is set"""
        u_at = datetime(2024, 1, 1)
        instance = BaseModel(updated_at=u_at)
        self.assertEqual(u_at, instance.updated_at)

    def test_init_raise_valueerror_when_updated_at_is_not_isoformat(self):
        """__init raises ValueError when passed invalid
        isoformat string to update_at"""
        u_at = 'invalid update_at isoformat string'
        with self.assertRaises(ValueError):
            BaseModel(updated_at=u_at)

    def test_init_ignore__class_key(self):
        """test __init ignores __class__ in **kwargs"""
        instance = BaseModel(__class__='User')
        self.assertEqual(
                instance.__class__,
                BaseModel)

    def test_save_call_storage_save_once(self):
        """test save calls storage.save method once"""
        instance = BaseModel()
        with patch(
                'models.base_model.BaseModel._BaseModel__storage.save'
                ) as p:
            instance.save()
        p.assert_called_once()

    def test_init_callstorage_new_when_kwargs_is_empty(self):
        """test BaseModel() call storage.new"""
        with patch('models.base_model.BaseModel._BaseModel__storage.new') as p:
            BaseModel()
        p.assert_called_once()
