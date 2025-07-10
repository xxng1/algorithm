from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(m):
    graph.append(list(map(int, input().split())))

visited = [ [False] * n for _ in range(m) ]
queue = deque()
def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    if len(queue) == 0:
        x, y = 0, 0
    else:
        x, y = queue.popleft()
    visited[x][y] = True
    queue.append((x, y))

    # graph[x][y] = True

    while queue:
        x, y = queue.popleft()
    
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if ( 0 <= nx < m and 0 <= ny < n ):
                if visited[nx][ny] == False:
                    if graph[nx][ny] != -1:
                        new_cost = graph[nx][ny]
                        if new_cost == 0 or new_cost > graph[x][y]:
                            graph[nx][ny] = graph[x][y] + 1
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                        
            



# bfs(0,1)
# bfs(3,5)
# 


# for i in range(m):
#     for j in range(n):
#         print(graph[i][j],end='')
#     print()


for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            # visited = [ [False] * n for _ in range(m) ]
            queue.append((i, j))




bfs()
            
# for i in visited:
#     print(i)

# for i in graph:
#     print(i)    



# for i in graph:
#     print(i)

maximum = -1e9
find_zero = False

# print(maximum)
for checkvalue in graph:
    if maximum < max(checkvalue):
        maximum = max(checkvalue)
    if 0 in checkvalue:
        find_zero = True


# print(maximum-1)
# print(find_zero)

if find_zero:
    print(-1)
else:
    print(maximum-1)

