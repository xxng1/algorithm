from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

for i in range(N):
    s = list(map(int, input().strip()))
    graph.append(s)

# print(graph)

visited = [[0]*M for _ in range(N)]
visited_break = [[0]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0] = 1

    while queue:
        x, y, broken = queue.popleft()
        
        if x == N-1 and y == M -1:
            if broken == 0:
                return visited[x][y]
            else:
                return visited_break[x][y]
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] ==0:
                    if broken == 0 and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny, 0))
                    elif broken == 1 and visited_break[nx][ny] == 0:
                        visited_break[nx][ny] = visited_break[x][y] + 1
                        queue.append((nx, ny, 1))
                
                elif broken == 0 and graph[nx][ny] == 1:
                    if visited_break[nx][ny] == 0:
                        visited_break[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny, 1))
    return -1          

print(bfs())
                        
# print(visited)                    
# print(visited_break)