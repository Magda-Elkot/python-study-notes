# Topic: Input & Output in Python

# ----------- OUTPUT -----------
# print() is used to display output to the console
print("Welcome to the Input & Output demo!")
print("This is an example of output using print().")

# ----------- INPUT -----------
# input() is used to get input from the user
# It always returns a string by default

# Get user's name
name = input("What is your name? ")
print("Hello,", name)

# Get user's age and convert it to an integer
age_str = input("How old are you? ")
age = int(age_str)  # convert string to integer
print("You are", age, "years old.")

# Combine input and output
print("Nice to meet you,", name + "! In 5 years, you will be", age + 5, "years old.")

# You can use f-string for cleaner output
print(f"{name}, in 5 years you will be {age + 5} years old.")
