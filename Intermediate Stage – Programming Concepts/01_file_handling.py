# Topic: Reading and Writing Files in Python

# -------- Writing to a file --------
# 'w' mode = write (creates file if not exists, overwrites if exists)
with open("example.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")

print("File written successfully.")

# -------- Reading from a file --------
# 'r' mode = read
with open("example.txt", "r") as file:
    content = file.read()

print("\n--- File content ---")
print(content)

# -------- Reading line by line --------
with open("example.txt", "r") as file:
    print("\n--- Reading line by line ---")
    for line in file:
        print(line.strip())  # strip removes \n at the end

# -------- Appending to a file --------
# 'a' mode = append (adds to end of file without erasing content)
with open("example.txt", "a") as file:
    file.write("This is an added line.\n")

print("\nLine appended successfully.")

# -------- Working with CSV files --------
import csv

# Writing CSV
with open("data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Magda", 23])
    writer.writerow(["El-Romany", 30])

# Reading CSV
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    print("\n--- CSV content ---")
    for row in reader:
        print(row)
