"""
=========================================================
BIT MANIPULATION — PYTHON NOTES (DSA + INTERVIEW)
=========================================================

Bit manipulation is widely used in:
- DSA problems
- Competitive programming
- Low-level optimization

This file covers:
1. Binary basics
2. Bitwise operators
3. Common tricks
4. Important formulas
5. DSA patterns
6. Interview questions
"""

# =========================================================
# =================== BINARY BASICS =======================
# =========================================================

"""
Decimal to Binary:
bin(5) -> '0b101'

Binary to Decimal:
int('101', 2) -> 5
"""

# =========================================================
# ================= BITWISE OPERATORS =====================
# =========================================================

"""
&  AND
|  OR
^  XOR
~  NOT
<< LEFT SHIFT
>> RIGHT SHIFT
"""

a = 5   # 101
b = 3   # 011

print(a & b)   # 1  -> 001
print(a | b)   # 7  -> 111
print(a ^ b)   # 6  -> 110
print(~a)      # -6 (two's complement)
print(a << 1)  # 10
print(a >> 1)  # 2

# =========================================================
# ================= COMMON BIT TRICKS =====================
# =========================================================

# --------------------------------------
# 1. CHECK EVEN / ODD
# --------------------------------------

def is_even(n):
    return (n & 1) == 0

# --------------------------------------
# 2. SET i-th BIT
# --------------------------------------

def set_bit(n, i):
    return n | (1 << i)

# --------------------------------------
# 3. CLEAR i-th BIT
# --------------------------------------

def clear_bit(n, i):
    return n & ~(1 << i)

# --------------------------------------
# 4. TOGGLE i-th BIT
# --------------------------------------

def toggle_bit(n, i):
    return n ^ (1 << i)

# --------------------------------------
# 5. CHECK i-th BIT
# --------------------------------------

def check_bit(n, i):
    return (n & (1 << i)) != 0

# =========================================================
# ================= COUNT SET BITS ========================
# =========================================================

# --------------------------------------
# Method 1: Built-in
# --------------------------------------

def count_bits_builtin(n):
    return bin(n).count("1")

# --------------------------------------
# Method 2: Brian Kernighan’s Algorithm
# --------------------------------------

def count_bits(n):
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count

# =========================================================
# ================= POWER OF TWO ==========================
# =========================================================

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# =========================================================
# ================= XOR PATTERNS ==========================
# =========================================================

"""
XOR Properties:
1. a ^ a = 0
2. a ^ 0 = a
3. XOR is commutative and associative
"""

# --------------------------------------
# Find single number (LeetCode classic)
# --------------------------------------

def single_number(arr):
    res = 0
    for x in arr:
        res ^= x
    return res

# =========================================================
# ================= SWAP USING XOR ========================
# =========================================================

def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b

# =========================================================
# ================= BIT MASKING ===========================
# =========================================================

"""
Bitmask is used to represent subsets
Example: 3 -> 011
"""

def subsets(nums):
    n = len(nums)
    result = []

    for mask in range(1 << n):
        temp = []
        for i in range(n):
            if mask & (1 << i):
                temp.append(nums[i])
        result.append(temp)

    return result

# =========================================================
# ================= DSA PATTERNS ==========================
# =========================================================

# --------------------------------------
# Missing number
# --------------------------------------

def missing_number(nums):
    xor = 0
    for i in range(len(nums) + 1):
        xor ^= i
    for x in nums:
        xor ^= x
    return xor

# --------------------------------------
# Two non-repeating numbers
# --------------------------------------

def two_unique(nums):
    xor = 0
    for x in nums:
        xor ^= x

    rightmost_set_bit = xor & -xor
    a = b = 0

    for x in nums:
        if x & rightmost_set_bit:
            a ^= x
        else:
            b ^= x
    return a, b

# =========================================================
# ================= INTERVIEW QUESTIONS ===================
# =========================================================

"""
Q: Why n & (n-1) removes lowest set bit?
A: n-1 flips all bits after the rightmost set bit

Q: Time complexity of bit ops?
A: O(1)

Q: Where used?
A: Flags, subsets, optimizations, CP
"""

print("Bit Manipulation notes loaded successfully.")
