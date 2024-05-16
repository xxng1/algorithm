import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt+=1


print(cnt)