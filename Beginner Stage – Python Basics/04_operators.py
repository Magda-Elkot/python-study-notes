# Topic: Operators in Python

# 1. Arithmetic Operators (+, -, *, /, %, //, **)
a = 10
b = 3

print("Addition:", a + b)         # 13
print("Subtraction:", a - b)      # 7
print("Multiplication:", a * b)   # 30
print("Division:", a / b)         # 3.333...
print("Floor Division:", a // b)  # 3 (drops decimal)
print("Modulus (remainder):", a % b)  # 1
print("Exponent:", a ** b)        # 1000

# 2. Comparison Operators (==, !=, >, <, >=, <=)
x = 5
y = 7

print("Equal:", x == y)         # False
print("Not equal:", x != y)     # True
print("Greater than:", x > y)   # False
print("Less than:", x < y)      # True
print("Greater or equal:", x >= y)  # False
print("Less or equal:", x <= y)     # True

# 3. Logical Operators (and, or, not)
is_adult = True
has_ticket = False

print("Allowed to enter?", is_adult and has_ticket)  # False
print("Allowed with one condition?", is_adult or has_ticket)  # True
print("Not adult:", not is_adult)  # False

# 4. Assignment Operators (=, +=, -=, etc.)
score = 10
print("Initial score:", score)

score += 5   # Same as: score = score + 5
print("After += 5:", score)

score *= 2   # score = score * 2
print("After *= 2:", score)

score -= 3
print("After -= 3:", score)

score /= 2
print("After /= 2:", score)
