import heapq
import sys

input = sys.stdin.readline
INF = 100000000

V, E = map(int, input().split())
K = int(input()) # start
dp = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, current = heapq.heappop(heap)

        if dp[current] < weight:
            continue
        for w, next_node in graph[current]:
            next_weight = w + weight
            if next_weight < dp[next_node]:
                dp[next_node] = next_weight
                heapq.heappush(heap, (next_weight, next_node))

Dijkstra(K)

for i in range(1, V+1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])