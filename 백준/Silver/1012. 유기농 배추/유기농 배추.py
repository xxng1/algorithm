from collections import deque

# cnt = 0
def bfs(x, y):
    # global cnt
    queue = deque()
    # 상 하 좌 우  | (1,0) -> (0, 0) = 상, (1,0) -> (1, 1) 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue.append((x, y))
    while(queue):
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0<= ny < N:
                if graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    graph[nx][ny] = 0
                    # for i in range(4):
                    #     nx = x + dx[i]
                    #     ny = y + dy[i]

                    #     if 0 <= nx < M and 0<= ny < N:
                    #         test[ny][nx] = 0
                            

T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]* N for _ in range(M)]
    for i in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1

    cnt = 0
    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1:
                bfs(a,b)
                cnt += 1
    
    print(cnt)