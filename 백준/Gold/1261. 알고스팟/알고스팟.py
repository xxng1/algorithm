from collections import deque

graph = []
N, M = map(int, input().split())

for _ in range(M):
    graph.append(list(map(int, input())))

visited = [[-1]*N for _ in range(M)]

def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[0][0] = 0

    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<M and 0<=ny<N and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft((nx, ny))
                else:
                    # visited[nx][ny] += 1
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    

bfs(0,0)
print(visited[M-1][N-1])
