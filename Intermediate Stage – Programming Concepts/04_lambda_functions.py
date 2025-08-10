# Topic: Lambda Functions, map, filter, reduce

# Lambda functions are small anonymous functions
# They are defined using the 'lambda' keyword instead of 'def'
# Syntax: lambda arguments: expression

from functools import reduce  # 'reduce' needs to be imported from functools

# -------- Basic lambda function --------
# This lambda takes two arguments x and y, and returns their sum
add = lambda x, y: x + y
print("Lambda add:", add(5, 3))  # Output: 8

# -------- Using lambda with map --------
# 'map()' applies a function to each element in an iterable (list, tuple, etc.)
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n ** 2, numbers))  # Each number squared
print("Squares (map + lambda):", squares)  # Output: [1, 4, 9, 16, 25]

# -------- Using lambda with filter --------
# 'filter()' returns elements that match a condition (True)
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))  # Keep only even numbers
print("Even numbers (filter + lambda):", even_numbers)  # Output: [2, 4]

# -------- Using lambda with reduce --------
# 'reduce()' applies a function cumulatively to elements, reducing them to one value
product = reduce(lambda x, y: x * y, numbers)  # Multiply all numbers together
print("Product (reduce + lambda):", product)  # Output: 120

# -------- Combining map and filter --------
# Here we filter even numbers first, then square them using map
even_squares = list(map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers)))
print("Even squares (map + filter + lambda):", even_squares)  # Output: [4, 16]