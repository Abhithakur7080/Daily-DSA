"""
=================================================
PYTHON LISTS — NOTES (DSA + INTERVIEW)
=================================================

This file covers:
- list basics
- creation methods
- indexing & slicing
- list operations
- built-in methods
- list comprehension
- common DSA patterns
- interview questions
"""

# --------------------------------------
# 1. WHAT IS A LIST?
# --------------------------------------
"""
- Ordered
- Mutable (can change)
- Allows duplicates
- Can store mixed data types
"""

arr = [1, 2, 3, 4]
mixed = [1, "a", 3.5, True]

# --------------------------------------
# 2. CREATING LISTS
# --------------------------------------

a = []
b = list()
c = [1, 2, 3]
d = list(range(5))        # [0,1,2,3,4]

# --------------------------------------
# 3. INDEXING
# --------------------------------------

nums = [10, 20, 30, 40]

print(nums[0])    # 10
print(nums[-1])   # 40

# --------------------------------------
# 4. SLICING
# --------------------------------------

print(nums[1:3])   # [20,30]
print(nums[:2])    # [10,20]
print(nums[2:])    # [30,40]
print(nums[::-1])  # reverse

# --------------------------------------
# 5. MODIFYING LIST
# --------------------------------------

nums[1] = 99       # [10,99,30,40]

# --------------------------------------
# 6. ADD ELEMENTS
# --------------------------------------

nums.append(50)           # add at end
nums.insert(1, 15)        # insert at index
nums.extend([60, 70])     # add multiple

# --------------------------------------
# 7. REMOVE ELEMENTS
# --------------------------------------

nums.remove(99)     # removes value
nums.pop()          # removes last
nums.pop(0)         # removes index
del nums[0]         # deletes element
nums.clear()        # clears list

# --------------------------------------
# 8. SEARCHING
# --------------------------------------

arr = [5, 3, 7, 1]

print(3 in arr)        # True
print(arr.index(7))   # 2
print(arr.count(3))   # 1

# --------------------------------------
# 9. SORTING & REVERSING
# --------------------------------------

arr.sort()            # ascending
arr.sort(reverse=True)
arr.reverse()

# --------------------------------------
# 10. LENGTH, MIN, MAX, SUM
# --------------------------------------

print(len(arr))
print(min(arr))
print(max(arr))
print(sum(arr))

# --------------------------------------
# 11. COPYING LIST
# --------------------------------------

a = [1, 2, 3]
b = a.copy()
c = a[:]              # slicing copy

# ❌ Wrong (same reference)
d = a

# --------------------------------------
# 12. LIST COMPREHENSION (IMPORTANT)
# --------------------------------------

squares = [x*x for x in range(5)]
even = [x for x in range(10) if x % 2 == 0]

# --------------------------------------
# 13. NESTED LISTS (2D ARRAY)
# --------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])   # 6

# --------------------------------------
# 14. ITERATION
# --------------------------------------

for x in arr:
    print(x)

for i in range(len(arr)):
    print(arr[i])

# --------------------------------------
# 15. COMMON DSA PATTERNS
# --------------------------------------

# Find max
def find_max(arr):
    mx = arr[0]
    for x in arr:
        if x > mx:
            mx = x
    return mx

# Reverse array
def reverse(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

# Check sorted
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# --------------------------------------
# 16. INTERVIEW QUESTIONS
# --------------------------------------

"""
Q: List vs Tuple?
A: List is mutable, tuple is immutable

Q: Time complexity of append?
A: O(1) amortized

Q: Remove vs Pop?
A: remove(value), pop(index)

Q: How to copy list?
A: copy(), slicing
"""

print("List notes loaded successfully.")
