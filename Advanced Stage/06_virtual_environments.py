# Topic: Virtual Environments in Python
# Virtual environments allow you to create isolated Python environments for different projects.
# This helps avoid conflicts between packages in different projects.

# -------- Why use Virtual Environments --------
# Imagine two projects: one needs Django 3.2, another needs Django 4.0
# Installing globally would create conflicts.
# Virtual environments solve this by isolating dependencies.

# -------- Creating a Virtual Environment --------
# In terminal (not inside Python):
# python3 -m venv myenv
# This creates a folder called 'myenv' with an isolated Python environment

# -------- Activating a Virtual Environment --------
# On Linux/macOS:
# source myenv/bin/activate
# On Windows (cmd):
# myenv\Scripts\activate.bat
# On Windows (PowerShell):
# myenv\Scripts\Activate.ps1

# Once activated, your shell prompt usually changes to show the environment name:
# (myenv) user@computer:~$

# -------- Installing Packages Inside a Virtual Environment --------
# Use pip as usual, it will only affect the virtual environment
# pip install requests
# pip list  # shows installed packages in the environment

# -------- Deactivating a Virtual Environment --------
# Simply run:
# deactivate
# This returns you to the global Python environment

# -------- Example: Using a Virtual Environment in a Project --------
# 1. Create virtual environment:
#    python3 -m venv venv
# 2. Activate:
#    source venv/bin/activate
# 3. Install packages:
#    pip install requests
# 4. Use in your Python scripts:
import requests

response = requests.get("https://api.github.com")
print("Status Code:", response.status_code)

# 5. Deactivate when done:
#    deactivate

# -------- Notes --------
# - Each project can have its own environment
# - Keep dependencies isolated for stability
# - Optionally, create a requirements file to save packages:
#    pip freeze > requirements.txt
# - To install from requirements:
#    pip install -r requirements.txt
