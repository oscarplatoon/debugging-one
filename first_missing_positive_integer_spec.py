import unittest
from first_missing_positive_integer import first_missing_positive

class FirstMissingPositiveMethods(unittest.TestCase):
  """ Tests for first_missing_positive_integer.py """

  def test_return_type(self):
      """ Test return value of first_missing_positive_integer """
      self.assertIsInstance(first_missing_positive([3,4,1,-2]), int)

  def test_empty_array(self):
      """ Test return value with empty array argument to function"""
      self.assertEqual(first_missing_positive([]), 1)

  def test_zero_array(self):
      """ Test return value with [0] to function"""
      self.assertEqual(first_missing_positive([0]), 1)
  
  def test_return_value(self):
    """ Test case to verify correct value is returned"""
    self.assertEqual(first_missing_positive([3,4,1,-2]), 2)

if __name__ == '__main__':
    unittest.main()