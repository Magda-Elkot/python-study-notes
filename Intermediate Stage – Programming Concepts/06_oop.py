# Topic: Object-Oriented Programming (OOP) in Python
# Covers: Classes, Objects, Inheritance, Magic Methods

# -------- Defining a Class --------
# A class is a blueprint for creating objects.
# Objects are instances of a class with their own data (attributes) and functions (methods).
class Person:
    # The __init__ method is the constructor.
    # It runs automatically when a new object is created.
    def __init__(self, name, age):
        # 'self' refers to the instance being created.
        self.name = name  # Instance variable for name
        self.age = age    # Instance variable for age

    # A normal method
    def greet(self):
        # Returns a greeting string
        return f"Hi, my name is {self.name} and I am {self.age} years old."

    # Magic Method: __str__
    # This is called automatically when we print the object.
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


# -------- Inheritance Example --------
# Student is a child class of Person (inherits its attributes and methods)
class Student(Person):
    # Child class constructor
    def __init__(self, name, age, student_id):
        # Call the parent constructor to set name and age
        super().__init__(name, age)
        # Add new attribute specific to Student
        self.student_id = student_id

    # Method Overriding:
    # We replace the greet() method from Person with our own version
    def greet(self):
        return f"Hello, I am {self.name}, a student with ID {self.student_id}."

    # Magic Method: __str__
    # Overrides the parent's __str__ method
    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, student_id={self.student_id})"


# -------- Creating Objects (Instances) --------
# Create a Person object
person1 = Person("Alice", 30)
print(person1.greet())  # Call greet method from Person
print(person1)          # Prints using __str__ method

# Create a Student object
student1 = Student("Bob", 20, "S12345")
print(student1.greet())  # Calls overridden greet() in Student
print(student1)          # Calls overridden __str__ in Student
