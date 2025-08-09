# Topic: Error Handling in Python

# -------- Basic try/except --------
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("That was not a valid number.")

# -------- Multiple exceptions --------
try:
    a = int(input("\nEnter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter only numbers.")
except ZeroDivisionError:
    print("You can't divide by zero!")

# -------- finally --------
try:
    file = open("some_file.txt", "w")
    file.write("Hello, world!")
finally:
    file.close()
    print("\nFile closed (finally block executed).")

# -------- Raising a custom exception --------
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age is valid: {age}")

try:
    check_age(-5)
except ValueError as e:
    print("Custom error:", e)
