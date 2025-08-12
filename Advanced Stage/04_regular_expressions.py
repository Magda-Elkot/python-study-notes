# Topic: Regular Expressions (re) in Python
# Regular expressions are patterns used to match strings.
# Python has a built-in module called `re` to work with them.

import re

# -------- Basic Matching --------
# re.search() finds the first match anywhere in the string
pattern = r"world"  # Raw string (r"") avoids needing to escape backslashes
text = "Hello world, welcome to Python!"

match = re.search(pattern, text)
if match:
    print(f"Found '{match.group()}' at position {match.start()}-{match.end()}")

print("\n---\n")

# -------- re.match() vs re.search() --------
# re.match() only checks the *beginning* of the string
match_start = re.match(r"Hello", text)
print("Match at start:", match_start.group() if match_start else "No match")

# re.search() can find it anywhere
match_anywhere = re.search(r"Python", text)
print("Match anywhere:", match_anywhere.group() if match_anywhere else "No match")

print("\n---\n")

# -------- Finding All Matches --------
# re.findall() returns all matches as a list
words = re.findall(r"\w+", text)  # \w+ matches "word characters" (letters, digits, underscore)
print("All words:", words)

# -------- Splitting by Regex --------
parts = re.split(r"\s+", text)  # Split on one or more spaces
print("Split by spaces:", parts)

print("\n---\n")

# -------- Replacing with re.sub() --------
# Replace all digits with '#'
sample = "My phone number is 123-456-7890"
hidden = re.sub(r"\d", "#", sample)
print("Phone hidden:", hidden)

print("\n---\n")

# -------- Special Patterns --------
# \d - digit, \w - word char, \s - whitespace
# ^ - start of string, $ - end of string
# [] - character set, () - capturing group, ? - optional, + - one or more, * - zero or more

email_pattern = r"[\w\.-]+@[\w\.-]+\.\w+"  # Basic email match
emails = "Contact us at support@example.com or sales@example.org"
found_emails = re.findall(email_pattern, emails)
print("Emails found:", found_emails)

print("\n---\n")

# -------- Using groups --------
date_text = "Today's date is 2025-08-12"
date_pattern = r"(\d{4})-(\d{2})-(\d{2})"  # Groups: year, month, day

match_date = re.search(date_pattern, date_text)
if match_date:
    year, month, day = match_date.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")
