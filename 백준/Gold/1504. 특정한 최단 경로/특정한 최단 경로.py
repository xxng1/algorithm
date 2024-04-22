import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
#K = int(input()) # start
#dp = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

def Dijkstra(start):
    dp = [INF]*(V+1)
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
        
    return dp

A = Dijkstra(1)
#v1 = 2
#v2 = 3

v1, v2 = map(int, input().split())

d1 = Dijkstra(v1)
d2 = Dijkstra(v2)

p1 = A[v1] + d1[v2] + d2[V]
p2 = A[v2] + d2[v1] + d1[V]

if min(p1, p2) < INF:
    print(min(p1, p2))
else:
    print(-1)