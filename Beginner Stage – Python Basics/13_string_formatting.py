# Topic: String Formatting in Python

name = "Magda"
age = 23

# Old style formatting
print("My name is %s and I am %d years old." % (name, age))

# str.format() method
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {0} and I am {1} years old.".format(name, age))

# f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# Formatting numbers
pi = 3.14159265
print("Pi to 2 decimal places: {:.2f}".format(pi))
print(f"Pi to 4 decimal places: {pi:.4f}")
