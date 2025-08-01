# Topic: Variables & Data Types

# Integer
age = 25

# When you want to print the word "age" (as text), put it inside quotes
print("Age:")

# When you want to print the value stored in the variable age, do NOT use quotes
print(age)

# Or combine both in one line:
print("Age:", age)  # "Age:" is a string, age is the variable

# Float
height = 5.9
print("Height:", height, "| Type:", type(height))

# String
name = "Magda"
print("Name:", name, "| Type:", type(name))

# Boolean
is_student = True
print("Is student:", is_student, "| Type:", type(is_student))

# Reassigning variables
age = age + 1
print("Next year age:", age)

# Type casting
age_str = str(age)
print("Age as string:", age_str, "| Type:", type(age_str))
