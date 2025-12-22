import heapq
import sys
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
dp = [INF] * (N+1)
chk = [0] * (N+1)

for _ in range(M):
    A, B, C = map(int,input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

def dijkstra(start):
    dp[start] = 0
    heap = []

    heapq.heappush(heap, (0, start))

    while heap:
        weight, current = heapq.heappop(heap)

        if dp[current] < weight:
            continue

        for w, next_node in graph[current]:
            next_weight = w + weight

            if dp[next_node] > next_weight:
                dp[next_node] = next_weight
                chk[next_node] = current
                heapq.heappush(heap, (next_weight, next_node))

# print(dp)

dijkstra(1)

# print(dp)
# print(chk)


print(N-1)
for i in range(2, N+1):
    print(chk[i], i)