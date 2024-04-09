import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dx = [ -1, -1, -1, 0, 0, 1, 1, 1]
    dy = [ 1, 0, -1, 1, -1, 1, 0, -1]
    graph[x][y] = 0 # 1
    queue = deque()
    queue.append((x,y))
    

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < h and 0<= ny < w:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx,ny))

while (True):
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    
    graph = []
    count = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)




