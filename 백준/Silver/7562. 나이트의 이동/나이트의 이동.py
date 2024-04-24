from collections import deque

def bfs(x, y):
    visited[x][y] = 1

    dx = [1, -1, 1, -1, 2, -2, 2, -2] # 이동 가능 x 배열
    dy = [2, 2, -2, -2, 1, 1, -1, -1] # 이동 가능 y 배열
    
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        
        if x == a and y == b:
                return visited[x][y] - 1
        
        for i in range(8):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
   
T = int(input())

for i in range(T):
    l = int(input())
    visited = [[0] * l for _ in range(l)]
    x, y = map(int, input().split())
    a, b = map(int, input().split())

    print(bfs(x, y))