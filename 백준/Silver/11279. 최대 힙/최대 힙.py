import heapq
import sys

input = sys.stdin.readline

N = int(input())
H = []
for i in range(N):
    x = int(input())
    if x == 0:
        if not H:
            print(0)
        else:
            print(heapq.heappop(H)[1])
    else:    
        heapq.heappush(H, (-x, x))