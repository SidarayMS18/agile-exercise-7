"""Tests for the calculator module.""" 
 
import unittest 
from calculator import Calculator 
 
class TestCalculator(unittest.TestCase): 
    """Test cases for Calculator class.""" 
    def setUp(self): 
        self.calc = Calculator() 
 
    def test_add(self): 
        """Test addition.""" 
        self.assertEqual(self.calc.add(2, 3), 5) 
 
    def test_subtract(self): 
        """Test subtraction.""" 
        self.assertEqual(self.calc.subtract(5, 3), 2) 
 
    def test_multiply(self): 
        """Test multiplication.""" 
        self.assertEqual(self.calc.multiply(4, 3), 12) 
 
    def test_divide(self): 
        """Test division.""" 
        self.assertEqual(self.calc.divide(10, 2), 5) 
        with self.assertRaises(ValueError): 
            self.calc.divide(10, 0) 
 
if __name__ == "__main__": 
    unittest.main()
