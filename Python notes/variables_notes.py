"""
========================================
PYTHON VARIABLES — COMPLETE NOTES
========================================

A variable is a name that refers to a value stored in memory.

Python variables:
- Do NOT need type declaration
- Are dynamically typed
- Can change type at runtime
"""

# --------------------------------------
# 1. BASIC VARIABLE ASSIGNMENT
# --------------------------------------

x = 10          # integer variable
y = 3.14        # float variable
name = "Abhi"   # string variable
is_active = True  # boolean variable

# --------------------------------------
# 2. DYNAMIC TYPING
# --------------------------------------

a = 5           # a is int
a = "five"      # now a is string (allowed in Python)

# --------------------------------------
# 3. MULTIPLE ASSIGNMENT
# --------------------------------------

p, q, r = 1, 2, 3   # assign multiple variables at once

# same value to multiple variables
i = j = k = 0

# --------------------------------------
# 4. VARIABLE NAMING RULES
# --------------------------------------

# Valid variable names
count = 10
_total = 50
userName = "Ram"
user_name = "Shyam"

# Invalid variable names (DO NOT USE)
# 2name = "A"       ❌ cannot start with number
# user-name = "B"   ❌ hyphen not allowed
# class = 10        ❌ reserved keyword

# --------------------------------------
# 5. VARIABLE TYPES (COMMON)
# --------------------------------------

num = 10                 # int
price = 99.99            # float
text = "Hello"           # str
flag = False             # bool
arr = [1, 2, 3]          # list
coords = (10, 20)        # tuple
unique = {1, 2, 3}       # set
person = {"name": "A"}  # dict

# --------------------------------------
# 6. CHECK VARIABLE TYPE
# --------------------------------------

x = 100
print(type(x))   # <class 'int'>

# --------------------------------------
# 7. VARIABLE SCOPE
# --------------------------------------

# GLOBAL VARIABLE
g = 10

def example():
    # LOCAL VARIABLE
    l = 5
    print(l)     # accessible here
    print(g)     # global accessible

# print(l) ❌ not accessible outside function

# --------------------------------------
# 8. CONSTANTS (BY CONVENTION)
# --------------------------------------

PI = 3.14159     # treated as constant (should not change)
MAX_LIMIT = 100

# Python does NOT enforce constants

# --------------------------------------
# 9. VARIABLE SWAPPING
# --------------------------------------

a = 5
b = 10

# Pythonic swap
a, b = b, a

# --------------------------------------
# 10. VARIABLE AS REFERENCE
# --------------------------------------

x = [1, 2, 3]
y = x            # y points to same object

y.append(4)
# x becomes [1,2,3,4] because both reference same list

# --------------------------------------
# 11. COPY VS REFERENCE
# --------------------------------------

# Shallow copy
a = [1, 2, 3]
b = a.copy()

b.append(4)
# a unchanged

# --------------------------------------
# 12. VARIABLE DELETION
# --------------------------------------

temp = 100
del temp         # variable removed from memory

# --------------------------------------
# 13. INPUT VARIABLES
# --------------------------------------

# x = int(input())                 # integer input
# arr = list(map(int, input().split()))  # list input

# --------------------------------------
# 14. VARIABLES IN DSA CONTEXT
# --------------------------------------

# Loop variables
for i in range(5):
    pass

# Temporary variables
temp = 0

# Pointer-style variables
left = 0
right = 5

# --------------------------------------
# 15. COMMON INTERVIEW POINTS
# --------------------------------------

"""
Q: Is Python pass-by-value or pass-by-reference?
A: Python is pass-by-object-reference.

Q: Can variable type change?
A: Yes (dynamic typing)

Q: Difference between None and 0?
A: None means no value, 0 is an integer
"""

print("Variables notes loaded successfully.")
