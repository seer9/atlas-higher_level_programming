#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id(self):
        base = Base()
        self.assertIsNotNone(base.id)