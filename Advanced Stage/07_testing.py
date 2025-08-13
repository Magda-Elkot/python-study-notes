# 07_testing.py
# Topic: Testing in Python
# Testing is a way to automatically check if your code works as expected.
# Python has two main ways to do this:
#   1. Built-in 'unittest' module (comes with Python)
#   2. Third-party 'pytest' library (you install separately)

# --------  Using unittest --------
import unittest  # import the unittest module

# Example function to test
def add(a, b):
    """Return the sum of a and b."""
    return a + b

# A test case is a class that inherits from unittest.TestCase
class TestMathFunctions(unittest.TestCase):

    # Every test method name must start with 'test_'
    def test_add_positive(self):
        # This checks if add(2, 3) returns 5
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        # This checks if add(-1, -1) returns -2
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        # This checks if add(0, 0) returns 0
        self.assertEqual(add(0, 0), 0)

# This block makes sure tests only run if we run this file directly
# and not when the file is imported as a module.
if __name__ == "__main__":
    unittest.main()  # This automatically finds all methods starting with 'test_' and runs them


# -------- Using pytest --------
# Pytest is a separate tool you install with: sudo pip install pytest
# It automatically finds test files and functions named 'test_*' and runs them.
# This style doesn't need classes unless you want them.

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def test_multiply_positive():
    # pytest uses plain assert instead of unittest's assertEqual
    assert multiply(3, 4) == 12

def test_multiply_zero():
    assert multiply(0, 5) == 0

def test_multiply_negative():
    assert multiply(-2, 3) == -6

# To run the pytest tests:
# 1. Save this file
# 2. In the terminal, run: pytest 07_testing.py
# Pytest will run ONLY the functions starting with 'test_'.
