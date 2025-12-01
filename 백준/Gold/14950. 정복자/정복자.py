import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

N, M, t = map(int, input().split())

edges = []
parent = [i for i in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
answer = 0
cnt = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        
        answer += ( cost + ( cnt * t ) ) 
        cnt += 1
        if cnt == N-1:
            break

print(answer)