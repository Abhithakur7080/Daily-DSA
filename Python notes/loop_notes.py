"""
=================================================
PYTHON LOOPS — NOTES (DSA + INTERVIEW)
=================================================

This file covers:
- for loop
- while loop
- range()
- break / continue / pass
- nested loops
- loop else
- common DSA patterns
- infinite loops
- time complexity intuition
"""

# --------------------------------------
# 1. FOR LOOP (BASIC)
# --------------------------------------

for i in range(5):
    print(i)    # 0 1 2 3 4

# --------------------------------------
# 2. FOR LOOP WITH START, END, STEP
# --------------------------------------

for i in range(1, 10, 2):
    print(i)    # 1 3 5 7 9

# --------------------------------------
# 3. LOOPING OVER COLLECTIONS
# --------------------------------------

nums = [10, 20, 30]

for num in nums:
    print(num)

# Loop with index
for idx, val in enumerate(nums):
    print(idx, val)

# --------------------------------------
# 4. WHILE LOOP
# --------------------------------------

i = 0
while i < 5:
    print(i)
    i += 1

# --------------------------------------
# 5. INFINITE LOOP (CONTROLLED)
# --------------------------------------

# while True:
#     user_input = input()
#     if user_input == "exit":
#         break

# --------------------------------------
# 6. BREAK STATEMENT
# --------------------------------------

for i in range(10):
    if i == 5:
        break
    print(i)

# --------------------------------------
# 7. CONTINUE STATEMENT
# --------------------------------------

for i in range(5):
    if i == 2:
        continue
    print(i)

# --------------------------------------
# 8. PASS STATEMENT
# --------------------------------------

for i in range(3):
    if i == 1:
        pass   # placeholder
    print(i)

# --------------------------------------
# 9. NESTED LOOPS
# --------------------------------------

for i in range(3):
    for j in range(3):
        print(i, j)

# --------------------------------------
# 10. LOOP ELSE (IMPORTANT INTERVIEW)
# --------------------------------------

for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")

# --------------------------------------
# 11. COMMON DSA PATTERNS
# --------------------------------------

# Print 1 to N
n = 5
for i in range(1, n + 1):
    print(i)

# Reverse loop
for i in range(n, 0, -1):
    print(i)

# Sum of array
arr = [1, 2, 3, 4]
total = 0
for num in arr:
    total += num

# --------------------------------------
# 12. COUNTING FREQUENCY
# --------------------------------------

s = "aabbbc"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# --------------------------------------
# 13. WHILE VS FOR (WHEN TO USE)
# --------------------------------------

"""
Use for:
- Known number of iterations
- Arrays / strings

Use while:
- Condition based loops
- Two pointer problems
"""

# --------------------------------------
# 14. TWO POINTER LOOP (DSA)
# --------------------------------------

arr = [1, 2, 3, 4, 5]
l, r = 0, len(arr) - 1

while l < r:
    print(arr[l], arr[r])
    l += 1
    r -= 1

# --------------------------------------
# 15. TIME COMPLEXITY INTUITION
# --------------------------------------

"""
Single loop        → O(n)
Nested loops       → O(n^2)
Loop inside while  → depends on updates
"""

print("Loops notes loaded successfully.")
