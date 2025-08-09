# Topic: List Comprehensions in Python

# -------- Basic List Comprehension --------
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print("Squares:", squares)

# -------- With a condition --------
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print("Even squares:", even_squares)

# -------- Converting strings --------
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print("Uppercase words:", upper_words)

# -------- Nested List Comprehensions --------
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)

# -------- Using functions inside comprehensions --------
def square(x):
    return x ** 2

squared_list = [square(n) for n in range(6)]
print("Squared list using function:", squared_list)
