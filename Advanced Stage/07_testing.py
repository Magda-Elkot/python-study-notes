# Topic: Testing in Python
# Testing ensures your code works as expected. Python has built-in 'unittest' and third-party 'pytest'.

# -------- Using unittest --------
import unittest

# Example function to test
def add(a, b):
    return a + b

# Create a test case class
class TestMathFunctions(unittest.TestCase):

    # Test method names must start with 'test_'
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)  # checks if 2+3 equals 5

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)  # checks negative numbers

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)  # checks zero addition

# Run tests
if __name__ == "__main__":
    unittest.main()  # runs all test cases in the class

# -------- Using pytest --------
# Pytest is simpler and more flexible than unittest
# Save this in a file called test_pytest_example.py
# To run: pytest test_pytest_example.py

def multiply(a, b):
    return a * b

def test_multiply_positive():
    assert multiply(3, 4) == 12  # simple assertion

def test_multiply_zero():
    assert multiply(0, 5) == 0

def test_multiply_negative():
    assert multiply(-2, 3) == -6
