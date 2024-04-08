import sys
input = sys.stdin.readline

n = int(input())
A, B = map(int, input().split())

m = int(input())
graph = [[] for i in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
visited = [0] * (n+1)
def dfs(start, cnt, find):
    #검문
    if start == find:
        return cnt
    visited[start] = 1

    # if find in graph[start]:
    #     return cnt
    for i in graph[start]:
        if visited[i] == 0:
            # visited[i] = 1
            # cnt += 1
            # dfs(i, cnt, find)
            result = dfs(i, cnt+1, find)
            if result != -1:
                return result
    return -1

print(dfs(A,0,B)) 