from collections import deque
N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for connections in arr:
    connections.sort()

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in (graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)                  

b_visited = [False] * (N+1)
d_visited = [False] * (N+1)
dfs(arr, V, d_visited)
print()
bfs(arr, V, b_visited)