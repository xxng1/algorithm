from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

visited = [[0 for _ in range(M)] for _ in range(N)]


for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            startx, starty = i, j

graph[startx][starty] = 0

def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((x, y))
    
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                    if visited[nx][ny] == 0:
                        if graph[nx][ny] == 1:
                            visited[nx][ny] = 1
                            graph[nx][ny] = graph[x][y] + 1
                            queue.append((nx, ny))

bfs(startx, starty)


for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and graph[i][j] == 1:
            graph[i][j] = -1

for i in graph:
    print(*i)