computer = int(input())

graph = [[] for _ in range(computer+1)]

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0] * (computer+1)

def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)

dfs(1)

count = 0
for i in visited:
    if i == 1:
        count += 1
        
print(count-1)