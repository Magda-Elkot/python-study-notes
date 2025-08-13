# Topic: Type Hinting & Annotations in Python
# Type hints are a way to specify expected data types for variables, function parameters, and return values.
# They help make your code easier to read and debug, and some tools (like mypy) can check them.

# -------- Basic Function Type Hinting --------
def greet(name: str) -> str:
    """Function expects a string and returns a string."""
    return f"Hello, {name}!"

print(greet("Alice"))

# -------- Multiple Parameter Types --------
def add_numbers(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b

print(add_numbers(5, 7))

# -------- Optional Parameters --------
from typing import Optional

def say_message(message: Optional[str] = None) -> str:
    """Parameter can be string or None."""
    if message:
        return message
    else:
        return "No message provided"

print(say_message("Hi there!"))
print(say_message())

# -------- Complex Types --------
from typing import List, Dict, Tuple

def process_scores(scores: List[int]) -> Dict[str, float]:
    """Accepts a list of integers and returns a dictionary with min, max, average."""
    return {
        "min": min(scores),
        "max": max(scores),
        "average": sum(scores)/len(scores)
    }

scores = [80, 90, 75, 88]
print(process_scores(scores))

# -------- Tuples --------
def get_name_and_age() -> Tuple[str, int]:
    """Returns a tuple (name, age)."""
    return "Bob", 30

name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")

# -------- Using type hints with functions as arguments --------
from typing import Callable

def call_func(func: Callable[[int, int], int], x: int, y: int) -> int:
    """Accepts a function taking two integers and returns an integer."""
    return func(x, y)

def multiply(a: int, b: int) -> int:
    return a * b

print(call_func(multiply, 4, 5))
