"""
=================================================
PYTHON FUNCTIONS — NOTES (DSA + INTERVIEW)
=================================================

This file covers:
- function definition
- parameters & arguments
- return vs print
- default / keyword / positional args
- *args and **kwargs
- recursion
- lambda functions
- scope (local / global)
- common DSA patterns
"""

# --------------------------------------
# 1. BASIC FUNCTION
# --------------------------------------

def greet():
    print("Hello")

greet()

# --------------------------------------
# 2. FUNCTION WITH PARAMETERS
# --------------------------------------

def add(a, b):
    return a + b

result = add(3, 4)

# --------------------------------------
# 3. RETURN vs PRINT (INTERVIEW)
# --------------------------------------

def square(x):
    return x * x      # returns value

def square_print(x):
    print(x * x)      # prints only

# --------------------------------------
# 4. DEFAULT PARAMETERS
# --------------------------------------

def power(base, exp=2):
    return base ** exp

power(3)      # 9
power(2, 3)   # 8

# --------------------------------------
# 5. POSITIONAL & KEYWORD ARGUMENTS
# --------------------------------------

def info(name, age):
    print(name, age)

info("A", 20)
info(age=25, name="B")

# --------------------------------------
# 6. *ARGS (VARIABLE LENGTH ARGUMENTS)
# --------------------------------------

def sum_all(*nums):
    total = 0
    for n in nums:
        total += n
    return total

sum_all(1, 2, 3, 4)

# --------------------------------------
# 7. **KWARGS (KEY-VALUE ARGUMENTS)
# --------------------------------------

def user_details(**data):
    for key, value in data.items():
        print(key, value)

user_details(name="A", age=22, city="Delhi")

# --------------------------------------
# 8. MIXING ARGS
# --------------------------------------

def mixed(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

# --------------------------------------
# 9. RECURSION (IMPORTANT FOR DSA)
# --------------------------------------

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# --------------------------------------
# 10. BASE CASE (VERY IMPORTANT)
# --------------------------------------

"""
Every recursive function must have:
1. Base case
2. Recursive call
"""

# --------------------------------------
# 11. FIBONACCI (RECURSIVE)
# --------------------------------------

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# --------------------------------------
# 12. LAMBDA FUNCTIONS
# --------------------------------------

square = lambda x: x * x
add = lambda a, b: a + b

# --------------------------------------
# 13. MAP, FILTER, REDUCE (COMMON)
# --------------------------------------

nums = [1, 2, 3, 4]

squared = list(map(lambda x: x * x, nums))
even = list(filter(lambda x: x % 2 == 0, nums))

# --------------------------------------
# 14. SCOPE (LOCAL / GLOBAL)
# --------------------------------------

x = 10

def test():
    x = 5      # local
    print(x)

def test_global():
    global x
    x = 20

# --------------------------------------
# 15. FUNCTION ANNOTATIONS
# --------------------------------------

def add(a: int, b: int) -> int:
    return a + b

# --------------------------------------
# 16. COMMON DSA FUNCTION PATTERNS
# --------------------------------------

# Max element
def find_max(arr):
    mx = arr[0]
    for x in arr:
        if x > mx:
            mx = x
    return mx

# Reverse array
def reverse(arr):
    return arr[::-1]

# Check palindrome
def is_palindrome(s):
    return s == s[::-1]

# --------------------------------------
# 17. INTERVIEW QUESTIONS
# --------------------------------------

"""
Q: Difference between return and print?
A: return gives value back, print just displays

Q: What is recursion?
A: Function calling itself

Q: When recursion fails?
A: No base case → stack overflow

Q: What is lambda?
A: One-line anonymous function
"""

print("Functions notes loaded successfully.")
