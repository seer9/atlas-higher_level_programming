#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id(self):
       
        base = Base()
        self.assertIsNotNone(base.id)

    def test_auto_assing_id(self):
        
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)

    def test_passed_id(self):
        
        base = Base(89)
        self.assertEqual(base.id, 89)

    def test_to_json_str_none(self):
      
        base_inst = Base()
        string = base_inst.to_json_str(None)
        self.assertEqual(string, '[]')