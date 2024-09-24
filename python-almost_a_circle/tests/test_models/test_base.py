#!/usr/bin/python3
import unittest
from models.base import Base
import json


class TestBase(unittest.TestCase):
    """Test class for Base"""

    def test_id(self):
        """Testing for an id"""
        Base.__nb_objects = 0
        base = Base()
        self.assertIsNotNone(base.id)
