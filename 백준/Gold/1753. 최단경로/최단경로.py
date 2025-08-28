import heapq


import sys

input = sys.stdin.readline


N, M = map(int, input().split())
K = int(input())

INF = float('inf')
graph = [ [] for _ in range(N+1)]
dp = [INF] * (N+1)
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

heap = []

def djstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, current = heapq.heappop(heap)
        
        if dp[current] < weight:
            continue

        for w, next_node in graph[current]:
            next_weight = w + weight

            if dp[next_node] > next_weight:
                dp[next_node] = next_weight
                heapq.heappush(heap, (next_weight, next_node))
djstra(K)

for i in range(1, len(dp)):
    if dp[i] == float('inf'):
        print("INF")
        continue
    print(dp[i])
    