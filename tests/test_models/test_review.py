#!/usr/bin/python3
"""This module defines class TestReview"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """contains test cases for class Review"""
    def test_place_id_exist_and_empty(self):
        """test class attribute place_id exist and empty"""
        self.assertTrue(
                hasattr(Review, 'place_id'),
                msg='Review.place_id is not here')
        self.assertEqual(
                Review.place_id, '',
                msg='Review.place_id should be empty')

    def test_user_id_exist_end_empty(self):
        """test class attribute user_id exist and empty initially"""
        self.assertTrue(
                hasattr(Review, 'user_id'),
                msg='Review.user_id is not here!')
        self.assertEqual(
                Review.user_id,
                '',
                msg='Review.user_id should be empty initially')

    def test_text_exist_and_empty(self):
        """test class attribute text exist and empty"""
        self.assertTrue(
                hasattr(Review, 'text'),
                msg='Review.text is not here!')
        self.assertEqual(
                Review.text,
                '',
                msg="Review.text should be initially empty!")
