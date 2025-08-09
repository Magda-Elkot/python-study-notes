# Topic: String Manipulation in Python

text = "  Python Programming  "

# Basic string methods
print("Original text:", text)
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Title case:", text.title())
print("Without spaces:", text.strip())  # remove spaces from start & end
print("Replace:", text.replace("Python", "Java"))

# Split and join
words = text.strip().split(" ")
print("Split into words:", words)
joined_text = "-".join(words)
print("Joined with dash:", joined_text)

# Find & check
print("Contains 'Python'?", "Python" in text)
print("Starts with 'Py'?", text.strip().startswith("Py"))
print("Ends with 'ing'?", text.strip().endswith("ing"))
