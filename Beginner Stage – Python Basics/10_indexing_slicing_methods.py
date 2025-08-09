# Topic: Indexing, Slicing, and Methods for Lists and Tuples

# ------- Indexing -------
numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])     # index 0
print("Last element:", numbers[-1])     # negative index

# ------- Slicing -------
print("From index 1 to 3:", numbers[1:4])  # stops at index 4 (exclusive)
print("First three:", numbers[:3])
print("From index 2 to end:", numbers[2:])
print("Every second element:", numbers[::2])

# ------- List Methods -------
numbers.append(60)
print("After append:", numbers)

numbers.remove(20)
print("After remove:", numbers)

numbers.sort()
print("After sort:", numbers)

numbers.reverse()
print("After reverse:", numbers)

# ------- Tuple indexing & slicing -------
colors = ("red", "green", "blue", "yellow")
print("First color:", colors[0])
print("Last two colors:", colors[-2:])
