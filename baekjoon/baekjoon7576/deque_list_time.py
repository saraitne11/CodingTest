import time
from collections import deque


a = list(range(100000))
b = deque(range(100000))

s = time.time()
for _ in range(50000):
    a.pop(0)
print(time.time() - s)

s = time.time()
for _ in range(50000):
    b.popleft()
print(time.time() - s)
