# Topic: Functions in Python (definition, parameters, return, scope)

# -----------------------------
# Basic function with no parameters
# -----------------------------
def greet():
    print("Hello from a function!")

greet()  # Call the function

# -----------------------------
# Function with parameters
# -----------------------------
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Magda")

# -----------------------------
# Function with return value
# -----------------------------
def add(a, b):
    return a + b

result = add(5, 3)
print("5 + 3 =", result)

# -----------------------------
# Function with default parameter
# -----------------------------
def welcome(name="Guest"):
    print(f"Welcome, {name}!")

welcome()           # uses default
welcome("Magda")    # uses provided value

# -----------------------------
# Scope example (local vs global)
# -----------------------------
def show_scope():
    x = 10  # local variable
    print("Inside function, x =", x)

x = 5  # global variable
show_scope()
print("Outside function, x =", x)  # global x is unchanged
