# Topic: Loops in Python (for, while, break, continue)

# ----------- FOR LOOP -----------
print("For loop from 1 to 5:")
for i in range(1, 6):  # 1 to 5 (6 is excluded)
    print(i)

# Loop through a list
fruits = ["apple", "banana", "cherry"]
print("\nLooping through a list:")
for fruit in fruits:
    print(fruit)

# ----------- WHILE LOOP -----------
print("\nWhile loop example:")
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# ----------- BREAK STATEMENT -----------
print("\nBreak example:")
for num in range(1, 10):
    if num == 5:
        print("Found 5, breaking the loop.")
        break
    print("Number:", num)

# ----------- CONTINUE STATEMENT -----------
print("\nContinue example (skip 3):")
for num in range(1, 6):
    if num == 3:
        continue  # skip number 3
    print("Number:", num)
