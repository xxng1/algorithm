from collections import deque
import heapq

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


queue = deque()
heap = []

for i in range(1, N+1):
    if indegree[i] == 0:
        # queue.append(i)
        heapq.heappush(heap, i)


# print(queue)
answer = []

while heap:
    now = heapq.heappop(heap)
    # now = queue.popleft()
    answer.append(now)
    
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            # queue.append(tmp)
            heapq.heappush(heap, next)
    # print(answer)

print(*answer)


