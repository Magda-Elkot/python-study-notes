# Topic: Conditional Statements (if, elif, else)

# Basic if statement
age = int(input("Enter your age: "))

if age >= 18:
    print("You're an adult.")
else:
    print("You're a minor.")

# Using elif to check multiple conditions
grade = int(input("Enter your grade (0-100): "))

if grade >= 90:
    print("You got an A.")
elif grade >= 80:
    print("You got a B.")
elif grade >= 70:
    print("You got a C.")
elif grade >= 60:
    print("You got a D.")
else:
    print("You failed.")

# Nested if example
has_ticket = input("Do you have a ticket? (yes/no): ")

if has_ticket == "yes":
    age = int(input("Enter your age again: "))
    if age >= 18:
        print("You may enter the event.")
    else:
        print("Sorry, you're too young.")
else:
    print("You need a ticket to enter.")
