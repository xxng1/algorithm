from collections import deque

N, M = map(int, input().split())

sadari = {}
bam = {}

for _ in range(N):
    a, b = map(int, input().split())
    sadari[a] = b

for _ in range(M):
    a, b = map(int, input().split())
    bam[a] = b




visited = [0] * 101
board = [0] * 101

def bfs(x):
    visited[x] = 1
    dx = [1, 2, 3, 4, 5, 6]
    queue = deque()
    queue.append((x))

    while queue:
        x = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            
            if 0 < nx <= 100 and visited[nx] == 0:
                if nx in sadari:
                    nx = sadari[nx]
                if nx in bam:
                    nx = bam[nx]

                if visited[nx] == 0:    
                    visited[nx] = 1
                    board[nx] = board[x] + 1
                    queue.append((nx))


bfs(1)
print(board[100])
