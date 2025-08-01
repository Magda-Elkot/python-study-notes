# Topic: Lists and Tuples in Python

# --------------------------
# LISTS
# --------------------------
# A list is a collection of items that can be changed (mutable)
fruits = ["apple", "banana", "cherry"]

print("Original list:", fruits)

# Access by index
print("First fruit:", fruits[0])

# Change an item
fruits[1] = "blueberry"
print("After changing second fruit:", fruits)

# Add items
fruits.append("orange")
print("After appending:", fruits)

# Remove items
fruits.remove("apple")
print("After removing apple:", fruits)

# Loop through a list
print("All fruits:")
for fruit in fruits:
    print("-", fruit)

# --------------------------
# TUPLES
# --------------------------
# A tuple is like a list, but it can't be changed (immutable)
colors = ("red", "green", "blue")

print("\nTuple of colors:", colors)

# Access by index
print("First color:", colors[0])

# Trying to change a tuple will cause an error
# colors[0] = "yellow"  # Uncommenting this will raise TypeError

# Tuples can be used for fixed collections
dimensions = (1920, 1080)
print("Screen resolution:", dimensions[0], "x", dimensions[1])
