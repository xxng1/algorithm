N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

visited = [ [0 for _ in range(M)] for _ in range(N)]

sz = 0

def dfs(x, y):
    global sz

    visited[y][x] = True
    cycle.append([x, y])

    if graph[y][x] == 'U' and y > 0:
        y -= 1
    elif graph[y][x] == 'D' and y < N-1:
        y += 1
    elif graph[y][x] == 'L' and x > 0:
        x -= 1
    elif graph[y][x] == 'R' and x < M-1:
        x += 1

    if visited[y][x] == 1:
        if [x, y] in cycle:
            sz += 1
    else:
        dfs(x, y)


for x in range(M):
    for y in range(N):
        if not visited[y][x]:
            cycle = []
            dfs(x, y)

print(sz)
    