"""
========================================
PYTHON NUMBERS — COMPLETE NOTES
========================================

Python supports multiple numeric data types:
- int
- float
- complex
- bool (subtype of int)
"""

# --------------------------------------
# 1. INTEGER (int)
# --------------------------------------

a = 10
b = -5
c = 0

# Python int has NO size limit
big = 10**100

# --------------------------------------
# 2. FLOAT (float)
# --------------------------------------

x = 10.5
y = -3.14
z = 1e3       # 1000.0 (scientific notation)

# Precision issue
print(0.1 + 0.2)  # 0.30000000000000004

# --------------------------------------
# 3. COMPLEX NUMBERS
# --------------------------------------

c1 = 3 + 4j
c2 = complex(2, -5)

# Access parts
real = c1.real
imag = c1.imag

# --------------------------------------
# 4. BOOLEAN (bool)
# --------------------------------------

t = True
f = False

# bool is subclass of int
print(True == 1)    # True
print(False == 0)   # True

# --------------------------------------
# 5. TYPE CHECKING
# --------------------------------------

type(10)        # int
type(10.5)      # float
type(3+2j)      # complex
type(True)      # bool

isinstance(10, int)    # True

# --------------------------------------
# 6. TYPE CONVERSION (CASTING)
# --------------------------------------

int(10.9)        # 10
float(5)         # 5.0
str(100)         # "100"

# Invalid conversion
# int("10.5") ❌ ValueError

int(float("10.5"))  # ✅ 10

# --------------------------------------
# 7. BASIC ARITHMETIC OPERATORS
# --------------------------------------

a, b = 10, 3

a + b   # addition
a - b   # subtraction
a * b   # multiplication
a / b   # division (float)
a // b  # floor division
a % b   # modulus
a ** b  # power

# --------------------------------------
# 8. FLOOR DIVISION DETAILS
# --------------------------------------

5 // 2     # 2
-5 // 2    # -3  (IMPORTANT INTERVIEW)

# --------------------------------------
# 9. MODULUS PROPERTIES
# --------------------------------------

-5 % 2    # 1
5 % -2    # -1

# --------------------------------------
# 10. COMPARISON OPERATORS
# --------------------------------------

a == b
a != b
a > b
a < b
a >= b
a <= b

# --------------------------------------
# 11. LOGICAL OPERATORS
# --------------------------------------

True and False
True or False
not True

# --------------------------------------
# 12. MATH MODULE (IMPORTANT)
# --------------------------------------

import math

math.sqrt(16)       # 4.0
math.floor(3.7)     # 3
math.ceil(3.2)      # 4
math.factorial(5)   # 120
math.gcd(12, 18)    # 6
math.lcm(4, 6)      # 12
math.log10(100)     # 2.0

# --------------------------------------
# 13. ABSOLUTE VALUE
# --------------------------------------

abs(-10)     # 10
abs(3+4j)    # 5.0

# --------------------------------------
# 14. ROUNDING
# --------------------------------------

round(3.6)       # 4
round(3.14159, 2) # 3.14

# --------------------------------------
# 15. POWER FUNCTIONS
# --------------------------------------

pow(2, 3)        # 8
pow(2, 3, 5)     # (2^3) % 5 → 3

# --------------------------------------
# 16. BITWISE OPERATORS (DSA)
# --------------------------------------

a = 5   # 101
b = 3   # 011

a & b   # AND → 1
a | b   # OR  → 7
a ^ b   # XOR → 6
~a      # NOT
a << 1  # left shift
a >> 1  # right shift

# --------------------------------------
# 17. CHECK EVEN / ODD
# --------------------------------------

n = 10
is_even = n % 2 == 0

# --------------------------------------
# 18. PRIME CHECK (BASIC)
# --------------------------------------

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# --------------------------------------
# 19. SWAPPING NUMBERS
# --------------------------------------

a, b = 10, 20
a, b = b, a   # Pythonic swap

# --------------------------------------
# 20. INPUT FOR DSA
# --------------------------------------

# n = int(input())
# a, b = map(int, input().split())

# --------------------------------------
# 21. COMMON INTERVIEW QUESTIONS
# --------------------------------------

"""
Q: Difference between / and // ?
A: / → float division
   // → floor division

Q: Why 0.1 + 0.2 != 0.3 ?
A: Floating point precision

Q: Is bool a number?
A: Yes, subclass of int

Q: Python int overflow?
A: No limit
"""

print("Numbers notes loaded successfully.")
