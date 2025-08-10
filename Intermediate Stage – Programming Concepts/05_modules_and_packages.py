# 05_modules_and_packages.py
# Topic: Modules and Packages in Python

# -------- Importing from our own module --------
import mymodule

print(mymodule.greet("Magda"))
print("Sum from mymodule:", mymodule.add_numbers(5, 7))
print("PI constant from mymodule:", mymodule.PI)

# -------- Importing specific functions --------
from mymodule import greet, add_numbers
print(greet("Python Learner"))
print("Sum using direct import:", add_numbers(10, 20))

# -------- Importing from built-in modules --------
import math
import datetime
import os

# Math module example
print("Square root of 16:", math.sqrt(16))

# Datetime module example
now = datetime.datetime.now()
print("Current date and time:", now)

# OS module example
print("Current working directory:", os.getcwd())
