# Topic: Command-Line Tools (argparse)
# This script demonstrates how to create a simple CLI (Command-Line Interface) tool in Python.

import argparse  # import library for parsing command-line arguments

# Create a parser object that will handle the arguments
parser = argparse.ArgumentParser(
    description="Simple CLI tool"
)

# Add a required argument called "--name"
# This argument must be provided when running the script
parser.add_argument(
    "--name",           # argument name
    type=str,           # data type of the argument
    required=True,      # makes this argument mandatory
    help="Enter your name"  # help message if user requests -h
)

# Add an optional argument called "--age"
# This argument is optional; the user can choose to provide it
parser.add_argument(
    "--age",
    type=int,
    help="Enter your age"  # help message
)

# Parse arguments from the command line
args = parser.parse_args()

# Use the parsed arguments in your program
print(f"Hello, {args.name}!")  # Always print the name

# Only print age if it was provided
if args.age:
    print(f"You are {args.age} years old.")

# ------------------------------
# HOW TO RUN THIS SCRIPT:
# Open terminal and navigate to the folder containing this file
# Run the script using python3 followed by the arguments:
#
# Example with both name and age:
# python3 04_command_line_tools.py --name Magda --age 23
#
# Output:
# Hello, Magda!
# You are 25 years old.
#
# Example with only name (age is optional):
# python3 04_command_line_tools.py --name Magda
#
# Output:
# Hello, Magda!
