from collections import deque, Counter
# deque

dq = deque([2, 3, 1])
print(dq) # deque([2, 3, 1])

dq.append(4)
print(dq) # deque([2, 3, 1, 4])

dq.appendleft(5)
print(dq) # deque([5, 2, 3, 1, 4])

dq.pop()
print(dq) # deque([5, 2, 3, 1])

dq.popleft()
print(dq) # deque([2, 3, 1])

dq.clear()
print(dq) # deque([])

dq.extend([2, 3, 1])
print(dq) # deque([2, 3, 1])

dq.extendleft([5, 4])
print(dq) # deque([4, 5, 2, 3, 1])

dq.rotate(1)
print(dq) # deque([1, 4, 5, 2, 3])

dq.rotate(-1)
print(dq) # deque([4, 5, 2, 3, 1])

dq.reverse()
print(dq) # deque([1, 3, 2, 5, 4])

dq.insert(2, 6)
print(dq) # deque([1, 3, 6, 2, 5, 4])

dq.remove(6)
print(dq) # deque([1, 3, 2, 5, 4])

dq.index(2)
print(dq) # deque([1, 3, 2, 5, 4])

dq.count(2)
print(dq) # deque([1, 3, 2, 5, 4])

# counter
arr = [1, 2, 2, 3, 4, 4, 4, 5]
print(Counter(arr)) # Counter({4: 3, 2: 2, 1: 1, 3: 1, 5: 1})
print(Counter(arr).most_common()) # [(4, 3), (2, 2), (1, 1), (3, 1), (5, 1)]
print(Counter(arr).most_common(2)) # [(4, 3), (2, 2)]
print(Counter(arr).most_common(2)[0]) # (4, 3)
print(Counter(arr).most_common(2)[0][0]) # 4
print(Counter(arr).most_common(2)[0][1]) # 3
print(Counter(arr).elements())