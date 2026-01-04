"""
========================================
PYTHON STRINGS — COMPLETE NOTES
========================================

Strings are:
- Immutable
- Sequence of characters
- Can be written in multiple ways
"""

# --------------------------------------
# 1. DIFFERENT WAYS TO CREATE STRINGS
# --------------------------------------

# Single quotes
s1 = 'Hello "Abhi"'

# Double quotes
s2 = "Abhi's code"

# Triple quotes (multiline / docstring)
s3 = """This is
Abhi's "code"
"""

# Triple single quotes also valid
s4 = '''Another
multiline
string'''

# --------------------------------------
# 2. STRING CONCATENATION
# --------------------------------------

a = "Hello"
b = "World"

# Using +
c = a + " " + b
# Result: "Hello World"

# Using join
c2 = " ".join([a, b])

# --------------------------------------
# 3. STRING REPETITION
# --------------------------------------

star = "*"
pattern = star * 5   # "*****"

# --------------------------------------
# 4. STRING INDEXING
# --------------------------------------

s = "Python"

# Positive indexing
first = s[0]   # 'P'

# Negative indexing
last = s[-1]   # 'n'

# --------------------------------------
# 5. STRING SLICING
# --------------------------------------

s = "Programming"

# s[start:end]
sub = s[0:6]      # "Progra"
sub2 = s[:4]      # "Prog"
sub3 = s[3:]      # "gramming"

# Step slicing
rev = s[::-1]     # reverse string

# --------------------------------------
# 6. STRINGS ARE IMMUTABLE
# --------------------------------------

s = "Hello"

# s[0] = 'h' ❌ ERROR (strings are immutable)

# Correct way
s = 'h' + s[1:]

# --------------------------------------
# 7. ESCAPE CHARACTERS
# --------------------------------------

text = "Hello\nWorld"   # newline
tab = "Hello\tWorld"    # tab
quote = "He said \"Hi\""

# --------------------------------------
# 8. RAW STRINGS
# --------------------------------------

path = r"C:\Users\Abhi\Desktop"
# Escape characters are ignored

# --------------------------------------
# 9. f-STRINGS (BEST WAY)
# --------------------------------------

name = "Abhi"
age = 23

msg = f"My name is {name} and age is {age}"

# Expressions allowed
calc = f"Sum = {10 + 20}"

# --------------------------------------
# 10. STRING METHODS (MOST IMPORTANT)
# --------------------------------------

s = "  hello World  "

# Case methods
s.upper()        # "  HELLO WORLD  "
s.lower()        # "  hello world  "
s.title()        # "  Hello World  "
s.capitalize()   # "  Hello world  "

# Trim spaces
s.strip()        # "hello World"
s.lstrip()
s.rstrip()

# Search
s.find("World")  # index or -1
s.index("World") # index or error

# Replace
s.replace("World", "Python")

# Split & Join
words = s.split()         # list of words
joined = "-".join(words)

# Check methods
s.isalpha()     # False
s.isdigit()     # False
"123".isdigit() # True
"s123".isalnum()# True

# Starts / Ends
s.startswith("  he")
s.endswith("ld  ")

# --------------------------------------
# 11. STRING COMPARISON
# --------------------------------------

a = "abc"
b = "ABC"

a == b      # False
a.lower() == b.lower()  # True

# --------------------------------------
# 12. STRING LENGTH
# --------------------------------------

len("Python")   # 6

# --------------------------------------
# 13. STRING ITERATION
# --------------------------------------

s = "ABC"
for ch in s:
    pass

# --------------------------------------
# 14. STRING INPUT (DSA)
# --------------------------------------

# s = input().strip()      # remove spaces
# arr = input().split()    # list of strings

# --------------------------------------
# 15. COMMON INTERVIEW QUESTIONS
# --------------------------------------

"""
Q: Are strings mutable?
A: No

Q: Difference between ' and " ?
A: No difference, both same

Q: Use of triple quotes?
A: Multiline strings & docstrings

Q: Fastest string formatting?
A: f-strings
"""

print("String notes loaded successfully.")
