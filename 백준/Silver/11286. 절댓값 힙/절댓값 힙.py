import heapq, sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
heap = []

# checklist = defaultdict()

for _ in range(N):
    x = int(input())

    if x == 0:
        if heap:
            a, b = heapq.heappop(heap)
            print(b)
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))
