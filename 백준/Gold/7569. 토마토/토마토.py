from collections import deque
import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())

graph = [[] for _ in range(H)]

# print(graph)

for i in range(H):
    for _ in range(N):
        graph[i].append(list(map(int, input().split())))

# print(graph[1])
# print(graph[0][0][1])

# [[0 1 0 0] [ 0 1 0 2 ]]


queue = deque()

for z in range(H):
    for i in range(N):
        for j in range(M):
            if graph[z][i][j] == 1:
                queue.append((z, i, j))

dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [-1, 1, 0, 0, 0, 0]

# print(queue)

while queue:
    z, y, x = queue.popleft()

    for i in range(6):
        nx = dx[i] + x
        ny = dy[i] + y
        nz = dz[i] + z
        
        if ( 0 <= nx < M and 0 <= ny < N and 0 <= nz < H):
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nz, ny, nx))

# for i in graph:
#     print(i)

maximum = -1e9
check_zero = False

for can in graph:
    for check_value in can:
        maximum = max(max(check_value), maximum)
        if 0 in check_value:
            check_zero = True

if check_zero:
    print(-1)
else:
    if maximum == 1 or maximum == -1:
        print(0)
    else:
        print(maximum-1)


# print(maximum)
# print(check_zero)