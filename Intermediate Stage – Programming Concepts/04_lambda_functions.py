# Topic: Lambda Functions, map, filter, reduce

from functools import reduce

# -------- Basic lambda function --------
add = lambda x, y: x + y
print("Lambda add:", add(5, 3))

# -------- Using lambda with map --------
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n ** 2, numbers))
print("Squares (map + lambda):", squares)

# -------- Using lambda with filter --------
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print("Even numbers (filter + lambda):", even_numbers)

# -------- Using lambda with reduce --------
product = reduce(lambda x, y: x * y, numbers)
print("Product (reduce + lambda):", product)

# -------- Combining map and filter --------
even_squares = list(map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers)))
print("Even squares (map + filter + lambda):", even_squares)
