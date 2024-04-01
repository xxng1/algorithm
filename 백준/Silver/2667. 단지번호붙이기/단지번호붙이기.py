N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count
    visited[x][y] = 1
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if graph[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)

count = 0
result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            count = 0
            dfs(i, j)
            result.append(count)

print(len(result))
for r in sorted(result):
    print(r)
