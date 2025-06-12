import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class"""
    
    def setUp(self):
        """Set up a calculator instance for all tests"""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test addition operation with various inputs"""
        # Positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
        # Negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-5, 10), 5)
        # Zero cases
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(0, 5), 5)
        # Floating point numbers
        self.assertAlmostEqual(self.calc.add(1.1, 2.2), 3.3, places=1)
    
    def test_subtraction(self):
        """Test subtraction operation with various inputs"""
        # Positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 5), 5)
        # Negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-5, 10), -15)
        # Zero cases
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        # Floating point numbers
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=1)
    
    def test_multiplication(self):
        """Test multiplication operation with various inputs"""
        # Positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 5), 50)
        # Negative numbers
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(-5, 10), -50)
        # Zero cases
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        # Floating point numbers
        self.assertAlmostEqual(self.calc.multiply(1.5, 2.5), 3.75, places=2)
        # Identity
        self.assertEqual(self.calc.multiply(1, 5), 5)
    
    def test_division(self):
        """Test division operation with various inputs"""
        # Normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        # Floating point results
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.333, places=3)
        # Division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        # Negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

if __name__ == '__main__':
    unittest.main()
