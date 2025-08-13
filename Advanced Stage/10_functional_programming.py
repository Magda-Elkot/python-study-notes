# Topic: Functional Programming Concepts in Python
# -------------------------------------------------
# Functional programming is a style of programming where you treat computation
# as the evaluation of mathematical functions and avoid changing state/mutable data.
# Key ideas: immutability, higher-order functions, pure functions.

from functools import reduce

# -------- 1. Pure Functions --------
# A pure function's output depends only on its inputs and has no side effects.
# Example: no printing, no modifying global variables, no reading/writing files.
def pure_add(a, b):
    return a + b  # Always produces the same output for the same inputs

print("Pure function result:", pure_add(2, 3))

# -------- 2. Higher-Order Functions --------
# A higher-order function is one that takes another function as an argument
# or returns a function as a result.

def apply_operation(func, x, y):
    # func is passed in as an argument and is applied to x and y
    return func(x, y)

print("Higher-order function (addition):", apply_operation(lambda a, b: a + b, 5, 7))
print("Higher-order function (multiplication):", apply_operation(lambda a, b: a * b, 5, 7))

# -------- 3. map() --------
# map(function, iterable) applies the function to each element of the iterable
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda n: n ** 2, numbers))
print("Squares using map:", squared)

# -------- 4. filter() --------
# filter(function, iterable) returns only the items where the function returns True
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print("Even numbers using filter:", even_numbers)

# -------- 5. reduce() --------
# reduce(function, iterable) reduces the iterable to a single value by repeatedly applying the function
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers using reduce:", product)

# -------- 6. Immutability Concept --------
# In functional programming, we avoid changing (mutating) existing data structures.
# Instead, we create new ones when we need changes.
original_list = [1, 2, 3]
new_list = original_list + [4]  # creates a new list, doesn't modify the original
print("Original list:", original_list)
print("New list:", new_list)

# -------- 7. Function Composition --------
# Combine multiple small functions into one
def double(x):
    return x * 2

def increment(x):
    return x + 1

# Composition: increment first, then double
result = double(increment(3))  # increment(3) -> 4, then double(4) -> 8
print("Function composition result:", result)
