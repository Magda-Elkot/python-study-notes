# Topic: Decorators in Python
# A decorator is a function that takes another function as an argument
# and extends its behavior without modifying the original function's code.

# -------- Basic Decorator --------
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()  # Call the original function
        print("After the function runs")
    return wrapper

@my_decorator  # Apply decorator to this function
def say_hello():
    print("Hello, World!")

say_hello()

print("\n---\n")

# -------- Decorator with Arguments --------
def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_decorator(3)  # Repeat 3 times
def greet(name):
    print(f"Hi {name}!")

greet("Magda")

print("\n---\n")

# -------- Practical Example: Timing Function Execution --------
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(1)  # Simulate a slow process
    print("Finished slow function")

slow_function()
