import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    a = int(input())
    heapq.heappush(heap, a)
    
# result = heapq.heappop(heap)

cnt = 0
result = 0

while cnt < N-1:
    # print(heap)
    if not heap:
        break

    data_1 = heapq.heappop(heap)
    data_2 = heapq.heappop(heap)
    
    result += ( data_1 + data_2 )
    
    heapq.heappush(heap, ( data_1 + data_2 ))
    cnt += 1


# print(heap)
print(result)