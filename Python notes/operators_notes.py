"""
=================================================
PYTHON CONDITIONAL & LOGICAL STATEMENTS — NOTES
=================================================

This file covers:
- if / elif / else
- logical operators
- comparison operators
- nested conditions
- ternary operator
- short-circuiting
- common interview traps
"""

# --------------------------------------
# 1. BASIC IF STATEMENT
# --------------------------------------

x = 10

if x > 5:
    print("x is greater than 5")

# --------------------------------------
# 2. IF-ELSE
# --------------------------------------

x = 3

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# --------------------------------------
# 3. IF-ELIF-ELSE (MULTIPLE CONDITIONS)
# --------------------------------------

score = 85

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "Fail"

# --------------------------------------
# 4. COMPARISON OPERATORS
# --------------------------------------

a, b = 10, 20

a == b   # equal
a != b   # not equal
a > b
a < b
a >= b
a <= b

# --------------------------------------
# 5. LOGICAL OPERATORS
# --------------------------------------

x = 10
y = 5

x > 5 and y < 10     # True
x > 15 or y < 10     # True
not (x > 5)          # False

# --------------------------------------
# 6. SHORT-CIRCUIT BEHAVIOR
# --------------------------------------

# AND stops at False
False and print("Not executed")

# OR stops at True
True or print("Not executed")

# --------------------------------------
# 7. NESTED IF
# --------------------------------------

x = 15

if x > 10:
    if x < 20:
        print("Between 10 and 20")

# --------------------------------------
# 8. MEMBERSHIP OPERATORS
# --------------------------------------

nums = [1, 2, 3]

2 in nums        # True
5 not in nums    # True

# --------------------------------------
# 9. IDENTITY OPERATORS
# --------------------------------------

a = [1, 2, 3]
b = a
c = [1, 2, 3]

a is b     # True (same memory)
a is c     # False (different object)
a == c     # True (same value)

# --------------------------------------
# 10. TERNARY OPERATOR
# --------------------------------------

x = 7
result = "Even" if x % 2 == 0 else "Odd"

# --------------------------------------
# 11. MULTIPLE CONDITIONS (CHAINING)
# --------------------------------------

x = 15
10 < x < 20    # True

# --------------------------------------
# 12. BOOLEAN CONVERSION (TRUTHY / FALSY)
# --------------------------------------

bool(0)        # False
bool(1)        # True
bool("")       # False
bool("abc")    # True
bool([])       # False
bool([1, 2])   # True
bool(None)     # False

# --------------------------------------
# 13. COMMON DSA CONDITIONS
# --------------------------------------

# Check positive / negative / zero
n = -5

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# Check leap year
year = 2024

is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# --------------------------------------
# 14. INPUT BASED CONDITIONS (DSA)
# --------------------------------------

# n = int(input())
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# --------------------------------------
# 15. COMMON INTERVIEW QUESTIONS
# --------------------------------------

"""
Q: Difference between == and is ?
A: == compares values
   is compares memory reference

Q: What is short-circuiting?
A: Evaluation stops early in and/or

Q: What values are False?
A: 0, 0.0, "", [], {}, (), None, False

Q: Is elif mandatory?
A: No

Q: Can if exist without else?
A: Yes
"""

print("Conditional & logical notes loaded successfully.")
