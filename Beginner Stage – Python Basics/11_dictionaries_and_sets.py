# Topic: Dictionaries and Sets in Python

# ------- Dictionary -------
person = {
    "name": "Magda",
    "age": 25,
    "city": "Matrouh"
}

print("Name:", person["name"])
person["age"] = 23  
person["country"] = "Egypt"  # add new key-value
print("Updated dictionary:", person)

# Loop through keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# ------- Set -------
fruits = {"apple", "banana", "cherry"}
print("Fruits set:", fruits)

fruits.add("orange")
print("After add:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

# Sets automatically remove duplicates
numbers = {1, 2, 2, 3, 4}
print("No duplicates:", numbers)
