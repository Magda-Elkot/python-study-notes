# Topic: Generators & Iterators in Python

# -------- Iterators --------
# An iterator is an object that allows us to traverse through all the elements in a collection (like a list),
# one element at a time, using the next() function.

numbers = [1, 2, 3]

# Get an iterator object from the list using iter()
iter_obj = iter(numbers)

# Use next() to get the next item from the iterator
print(next(iter_obj))  # Prints 1 (the first item)
print(next(iter_obj))  # Prints 2 (the second item)
print(next(iter_obj))  # Prints 3 (the third item)

# If you call next() again, it will raise StopIteration because there are no more items.
# Uncommenting the next line will cause an error:
# print(next(iter_obj))

print("\n---\n")

# -------- Generators --------
# Generators are special functions that return an iterator.
# Instead of returning all values at once, they yield them one at a time,
# saving memory and allowing iteration over large or infinite sequences.

def count_up_to(max):
    count = 1
    # Loop from 1 up to max (inclusive)
    while count <= max:
        yield count  # Yield pauses here and returns the current count
        count += 1   # After resuming, increment count and loop again

# Create a generator object by calling the function
counter = count_up_to(5)

# We can iterate through the generator with a for loop
for num in counter:
    print(num)  # Prints numbers 1 through 5, one at a time

print("\n---\n")

# -------- Generator Expressions --------
# Similar to list comprehensions, but they generate values one at a time (lazy evaluation)
# which is more memory efficient for large datasets.

# This creates a generator that yields squares of numbers 1 to 5
squares = (x ** 2 for x in range(1, 6))

print(squares)  # Prints something like <generator object ...> — it's a generator object

# To get the values, we iterate over it
for sq in squares:
    print(sq)  # Prints 1, 4, 9, 16, 25
