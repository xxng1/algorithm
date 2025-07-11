from collections import deque
import sys

input = sys.stdin.readline

T = int(input())


# visited = [[0] * M for _ in range(N)]





def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[y][x] = 1

    queue = deque()
    queue.append((y, x))
    
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if ( 0 <= nx < M and 0 <= ny < N):
                if ( visited[ny][nx] == 0 and graph[ny][nx] == 1 ):
                    visited[ny][nx] = 1
                    queue.append((ny, nx))

# print(graph[1][1])
# for i in graph:
#     print(i)

# print('----')


# for i in visited:
#     print(i)

# print('----')
# bfs(0,0)

# for i in visited:
#     print(i)


for TestCase in range(T):
    cnt = 0
    

    M, N, K = map(int, input().split())
    visited = [[0] * M for _ in range(N)]

    graph = [[0] * M for _ in range(N)]


    for _ in range(K):
        a, b = map(int, input().split())
    
        graph[b][a] = 1


    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == 0:
                bfs(j, i)
                cnt += 1

    # for i in visited:
    #     print(i)

    print(cnt)