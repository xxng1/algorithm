import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

visited = [[False]*C for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0

def dfs(x, y, dist):
    global ans

    if x == 0 and y == C - 1:
        if dist == K:
            ans += 1
        return

    if dist >= K:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and board[nx][ny] != 'T':
                visited[nx][ny] = True
                dfs(nx, ny, dist + 1)
                visited[nx][ny] = False


visited[R-1][0] = True
dfs(R-1, 0, 1)

print(ans)