from collections import deque
N = int(input())

A = deque([])
# A = deque([1, 2, 3, 4])
for i in range(1, N+1):
    A.append(i)

while True:
    if len(A) == 1:
        break

    A.popleft()
    A.append(A.popleft())

print(A.pop())