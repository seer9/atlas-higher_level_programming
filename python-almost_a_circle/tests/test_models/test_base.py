#!/usr/bin/python3
import unittest
from models.base import Base
import json


class TestBase(unittest.TestCase):
    """Test class for Base"""

    def test_id(self):
        """Testing for auto assign id"""
        base = Base()
        self.assertIsNotNone(base.id)
