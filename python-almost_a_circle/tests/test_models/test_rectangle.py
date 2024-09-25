import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
      """test if rectangle(1, 2) exists"""
      rect = Rectangle(1, 2)
      self.assertIsInstance(rect, Rectangle)
      self.assertEqual(rect.width, 1)
      self.assertEqual(rect.height, 2)

      """test if rectangle(1, 2, 3) exists"""
      rect2 = Rectangle(1, 2, 3)
      self.assertIsInstance(rect2, Rectangle)
      self.assertEqual(rect2.width, 1)
      self.assertEqual(rect2.height, 2)
      self.assertEqual(rect2.x, 3)

      """test if rectangle(1, 2, 3, 4) exists"""
      rect3 = Rectangle(1, 2, 3, 4)
      self.assertIsInstance(rect3, Rectangle)
      self.assertEqual(rect3.width, 1)
      self.assertEqual(rect3.height, 2)
      self.assertEqual(rect3.x, 3)
      self.assertEqual(rect3.y, 4)

      """test if rectangle(1, 2, 3, 4, 5) exists"""
      rect4 = Rectangle(1, 2, 3, 4, 5)
      self.assertIsInstance(rect4, Rectangle)
      self.assertEqual(rect4.width, 1)
      self.assertEqual(rect4.height, 2)
      self.assertEqual(rect4.x, 3)
      self.assertEqual(rect4.y, 4)
      self.assertEqual(rect4.id, 5)


    def test_invalid_init(self):
      """test if rectangle("1", 2) raises a TypeError"""
      with self.assertRaises(TypeError):
        rect = Rectangle("1", 2)

      """test if rectangle(1, "2") raises a TypeError"""
      with self.assertRaises(TypeError):
        rect = Rectangle(1, "2")

      """test if rectangle(1, 2, "3") raises a TypeError"""
      with self.assertRaises(TypeError):
        rect = Rectangle(1, 2, "3")

      """test if rectangle(1, 2, 3, "4") raises a TypeError"""
      with self.assertRaises(TypeError):
        rect = Rectangle(1, 2, 3, "4")

      """test if rectangle(-1, 2) raises a ValueError"""
      with self.assertRaises(ValueError):
        rect = Rectangle(-1, 2)

      """test if rectangle(1, -2) raises a ValueError"""
      with self.assertRaises(ValueError):
        rect = Rectangle(1, -2)

  