# Topic: Context Managers in Python
# Context managers help manage resources like files or network connections,
# making sure they are properly acquired and released (e.g., opened and closed).

# -------- The problem without context managers --------
# When working with files, you must remember to close the file after opening it.
# Forgetting to close a file can lead to resource leaks.

file = open("example.txt", "w")
file.write("Hello, world!")
file.close()  # You must close the file manually

print("File written and closed manually.\n")

# -------- Using a context manager with 'with' --------
# The 'with' statement automatically handles opening and closing the file,
# even if errors occur inside the block.

with open("example.txt", "w") as file:
    file.write("Hello from a context manager!")

# No need to call file.close() — it's done automatically

print("File written and closed automatically by 'with' block.\n")

# -------- How context managers work internally --------
# You can create your own context manager by defining a class
# that has __enter__() and __exit__() methods.

class MyContextManager:
    def __enter__(self):
        # This runs when entering the 'with' block
        print("Entering the context")
        return self  # This object can be assigned to a variable after 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        # This runs when exiting the 'with' block
        # exc_type, exc_val, exc_tb contain exception info if an error occurred, else None
        print("Exiting the context")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        # Return False to propagate the exception, True to suppress it
        return False

# Using the custom context manager
with MyContextManager() as cm:
    print("Inside the with block")
    # Uncomment the next line to see exception handling in action
    # raise ValueError("Oops, something went wrong!")

print("\nDone with custom context manager.\n")

# -------- Context managers using 'contextlib' --------
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Before yield (entering)")
    yield  # Code here is where the 'with' block runs
    print("After yield (exiting)")

with my_context():
    print("Inside the 'with' block using contextlib")

print("\nFinished contextlib example.\n")
