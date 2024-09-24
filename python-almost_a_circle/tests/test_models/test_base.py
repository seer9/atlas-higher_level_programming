#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id(self):
       
        b1 = Base()
        self.assertIsNotNone(b1.id)
