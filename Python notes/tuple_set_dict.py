"""
=========================================================
PYTHON TUPLE, SET & DICTIONARY — NOTES (DSA + INTERVIEW)
=========================================================

This file covers:
1. Tuple (immutable sequence)
2. Set (unique unordered collection)
3. Dictionary (key-value pairs)
With:
- creation
- operations
- methods
- DSA patterns
- interview questions
"""

# =========================================================
# ======================= TUPLE ===========================
# =========================================================

"""
TUPLE PROPERTIES:
- Ordered
- Immutable
- Allows duplicates
- Faster than list
"""

# --------------------------------------
# 1. CREATING TUPLES
# --------------------------------------

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = tuple([4, 5, 6])

# --------------------------------------
# 2. INDEXING & SLICING
# --------------------------------------

t = (10, 20, 30, 40)

print(t[0])
print(t[-1])
print(t[1:3])

# --------------------------------------
# 3. IMMUTABILITY
# --------------------------------------

# ❌ t[0] = 99  # Error

# --------------------------------------
# 4. TUPLE METHODS
# --------------------------------------

print(t.count(20))
print(t.index(30))

# --------------------------------------
# 5. UNPACKING
# --------------------------------------

a, b, c = (1, 2, 3)
x, *y = (10, 20, 30, 40)

# --------------------------------------
# 6. USE CASES
# --------------------------------------
"""
- Fixed data
- Dictionary keys
- Faster iteration
"""

# =========================================================
# ======================== SET ============================
# =========================================================

"""
SET PROPERTIES:
- Unordered
- Mutable
- No duplicates
"""

# --------------------------------------
# 7. CREATING SETS
# --------------------------------------

s1 = set()
s2 = {1, 2, 3, 4}
s3 = set([1, 2, 2, 3])  # duplicates removed

# --------------------------------------
# 8. ADD & REMOVE
# --------------------------------------

s2.add(5)
s2.remove(2)
s2.discard(10)   # no error if not present
s2.pop()         # removes random element
s2.clear()

# --------------------------------------
# 9. SET OPERATIONS
# --------------------------------------

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # union
print(a & b)   # intersection
print(a - b)   # difference
print(a ^ b)   # symmetric difference

# --------------------------------------
# 10. SUBSET / SUPERSET
# --------------------------------------

print({1, 2}.issubset(a))
print(a.issuperset({1}))

# --------------------------------------
# 11. COMMON DSA USE CASE
# --------------------------------------

# Remove duplicates
arr = [1, 2, 2, 3, 4]
unique = list(set(arr))

# =========================================================
# ===================== DICTIONARY ========================
# =========================================================

"""
DICTIONARY PROPERTIES:
- Key-value pair
- Keys are unique
- Mutable
"""

# --------------------------------------
# 12. CREATING DICTIONARY
# --------------------------------------

d1 = {}
d2 = {"a": 1, "b": 2}
d3 = dict(x=10, y=20)

# --------------------------------------
# 13. ACCESSING VALUES
# --------------------------------------

print(d2["a"])
print(d2.get("c", 0))   # safe access

# --------------------------------------
# 14. ADD / UPDATE
# --------------------------------------

d2["c"] = 3
d2.update({"d": 4})

# --------------------------------------
# 15. DELETE
# --------------------------------------

del d2["a"]
d2.pop("b")
d2.clear()

# --------------------------------------
# 16. ITERATION
# --------------------------------------

data = {"a": 1, "b": 2}

for key in data:
    print(key)

for value in data.values():
    print(value)

for k, v in data.items():
    print(k, v)

# --------------------------------------
# 17. FREQUENCY MAP (IMPORTANT DSA)
# --------------------------------------

def freq_map(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq

# --------------------------------------
# 18. SORT DICTIONARY
# --------------------------------------

d = {"a": 3, "b": 1, "c": 2}

sorted_by_key = dict(sorted(d.items()))
sorted_by_value = dict(sorted(d.items(), key=lambda x: x[1]))

# --------------------------------------
# 19. COMMON DSA PATTERNS
# --------------------------------------

# First non-repeating element
def first_unique(arr):
    freq = freq_map(arr)
    for x in arr:
        if freq[x] == 1:
            return x
    return -1

# --------------------------------------
# 20. INTERVIEW QUESTIONS
# --------------------------------------

"""
Q: Tuple vs List?
A: Tuple immutable, list mutable

Q: Set vs List?
A: Set removes duplicates, unordered

Q: Dict vs Map?
A: Python dict is hash map

Q: Time complexity of dict lookup?
A: O(1) average
"""

print("Tuple, Set & Dict notes loaded successfully.")
