"""
===========================================================
Python Built-in Functions & Utilities – DSA Ready Notes
===========================================================

Author  : Abhijeet Kumar
Purpose : Learn & revise Python built-ins used in DSA
Level   : Beginner → Intermediate
-----------------------------------------------------------

This file covers:
- Custom length calculation
- Sorting (ascending, descending, key-based)
- min / max with keys
- sum & product
- any() & all()
- enumerate()
- reversed()
- range()

Use this as:
✔ DSA revision notes
✔ Interview preparation
✔ Python fundamentals reference
"""

import math


# -----------------------------------------------------------
# 1. Length of a String (Without using len())
# -----------------------------------------------------------

def length_of_string(s):
    """
    Returns length of string without using len()
    Time Complexity : O(n)
    Space Complexity: O(1)
    """
    count = 0
    for _ in s:
        count += 1
    return count


print("Length of 'Abhijeet':", length_of_string("Abhijeet"))


# -----------------------------------------------------------
# 2. Sorting Lists
# -----------------------------------------------------------

# Ascending Order
arr = [1, 5, 7, 3, 6]
print("\nAscending Order:")
print(sorted(arr))   # does NOT modify original list

arr.sort()            # modifies original list
print(arr)


# Descending Order
arr2 = [1, 5, 7, 3, 6]
print("\nDescending Order:")
print(sorted(arr2, reverse=True))

arr2.sort(reverse=True)
print(arr2)


# Sorting based on absolute value
arr3 = [-1, 5, -7, 3, -6]
print("\nSort by Absolute Value:")
print(sorted(arr3, key=abs))

arr3.sort(key=abs)
print(arr3)


# Sorting strings based on length
fruits = ["apple", "banana", "pine apple", "guava", "mango"]

print("\nSort Strings by Length (Ascending):")
fruits.sort(key=len)
print(fruits)

print("\nSort Strings by Length (Descending):")
fruits.sort(key=len, reverse=True)
print(fruits)


# -----------------------------------------------------------
# 3. Minimum & Maximum
# -----------------------------------------------------------

fruits = ["apple", "banana", "pine apple", "guava", "mango"]

print("\nMinimum & Maximum:")
print("Min (lexicographical):", min(fruits))
print("Max (lexicographical):", max(fruits))
print("Min (by length):", min(fruits, key=len))
print("Max (by length):", max(fruits, key=len))

arr = [-1, 5, -7, 3, -6]
print("Min (by abs):", min(arr, key=abs))
print("Max (by abs):", max(arr, key=abs))


# -----------------------------------------------------------
# 4. Sum of Elements
# -----------------------------------------------------------

arr = [1, 5, 7, 3, 6]
print("\nSum:")
print(sum(arr))
print(sum(arr, 10))           # start value
print(sum(arr, start=10))


# -----------------------------------------------------------
# 5. Product of Elements
# -----------------------------------------------------------

print("\nProduct:")
print(math.prod(arr))


# -----------------------------------------------------------
# 6. any() – Logical OR
# -----------------------------------------------------------

print("\nany():")
print(any([False, True, True]))
print(any([False, False, False]))
print(any([1, 5, 7, 3, 6]))


# -----------------------------------------------------------
# 7. all() – Logical AND
# -----------------------------------------------------------

print("\nall():")
print(all([False, True, True]))
print(all([False, False, False]))
print(all([1, 5, 7, 3, 6]))


# -----------------------------------------------------------
# 8. enumerate() – Index + Value
# -----------------------------------------------------------

arr = [1, 5, 7, 3, 6]

print("\nenumerate():")
for i, val in enumerate(arr):
    print(i, val)

print("\nUsing range(len()):")
for i in range(len(arr)):
    print(i, arr[i])


# -----------------------------------------------------------
# 9. Reversing a List
# -----------------------------------------------------------

arr = [1, 5, 7, 3, 6]

print("\nReversed (without modifying original):")
print(list(reversed(arr)))

print("Original List:", arr)

arr.reverse()
print("Reversed In-place:", arr)


# -----------------------------------------------------------
# 10. range()
# -----------------------------------------------------------

print("\nrange():")
print(list(range(10)))
print(list(range(1, 10)))
print(list(range(1, 10, 2)))


# -----------------------------------------------------------
# END OF FILE
# -----------------------------------------------------------

"""
Quick Interview Notes:
----------------------
✔ sorted() → returns new list
✔ sort() → modifies original list
✔ key= is used for custom sorting
✔ any() → at least one True
✔ all() → all must be True
✔ enumerate() → best for index + value
✔ reversed() → iterator, non-destructive
✔ reverse() → in-place
"""
