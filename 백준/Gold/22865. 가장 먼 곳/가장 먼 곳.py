import heapq
import sys

input = sys.stdin.readline

N = int(input())

A, B, C = map(int, input().split())

M = int(input())

graph = [ [] for _ in range(N+1) ]
INF = float('inf')

for _ in range(M):
    D, E, L = map(int, input().split())
    graph[D].append((E, L))
    graph[E].append((D, L))

def dijkstra(start, graph, N):
    dp = [INF] * (N+1)
    dp[start] = 0
    heap = [(0, start)]
    
    while heap:
        cost, node = heapq.heappop(heap)
        
        if dp[node] < cost:
            continue

        for nxt_node, nxt_cost in graph[node]:
            nxt_cost = cost + nxt_cost
            
            if nxt_cost < dp[nxt_node]:
                dp[nxt_node] = nxt_cost
                heapq.heappush(heap, (nxt_cost, nxt_node))
    return dp

dpa = dijkstra(A, graph, N)
dpb = dijkstra(B, graph, N)
dpc = dijkstra(C, graph, N)

# ans = 0

max_dist = -1
result = 0

for i in range(1, N+1):
    # print(dpa[i], dpb[i], dpc[i])
    min_dist = min(dpa[i], dpb[i], dpc[i])
    
    if min_dist > max_dist:
        max_dist = min_dist
        result = i
    # print(min_dist, max_dist)

print(result)
        
