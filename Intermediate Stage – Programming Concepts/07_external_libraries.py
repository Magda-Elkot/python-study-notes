# Topic: Working with External and Built-in Python Libraries
# Covers: pip, requests, datetime, os, math

# -------- Installing an external library --------
# Run this in your terminal (not inside Python) to install 'requests':
# pip install requests

# -------- Using an external library: requests --------
import requests

# Send a GET request to fetch data from a URL
response = requests.get("https://api.github.com")
# Check status code (200 means OK)
print("Status Code:", response.status_code)
# Show part of the JSON response
print("GitHub API info:", response.json()["current_user_url"])

# -------- Using built-in library: datetime --------
import datetime

# Get the current date and time
now = datetime.datetime.now()
print("Current Date and Time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

# -------- Using built-in library: os --------
import os

# Get the current working directory
print("Current working directory:", os.getcwd())

# List all files in the current directory
print("Files in directory:", os.listdir("."))

# -------- Using built-in library: math --------
import math

# Perform some math operations
print("Square root of 25:", math.sqrt(25))
print("Pi constant from math module:", math.pi)
print("Factorial of 5:", math.factorial(5))
