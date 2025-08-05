from collections import deque
import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 거리 기록용
dist = [[-1]*M for _ in range(N)]

def bfs():
    queue = deque()
    queue.append((0, 0))
    dist[0][0] = 0

    sword_time = float('inf')

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if dist[nx][ny] == -1:
                    # 벽이 아닌 경우
                    if arr[nx][ny] != 1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))

                        # 검을 먹은 경우: 그 시점 거리 + 벽 무시 최단 거리
                        if arr[nx][ny] == 2:
                            sword_time = dist[nx][ny] + (N - 1 - nx) + (M - 1 - ny)

    # 공주에게 도달한 경우 거리
    normal_time = dist[N-1][M-1]

    # 두 가지 경우 중 작은 것
    answer = float('inf')
    if normal_time != -1:
        answer = min(answer, normal_time)
    if sword_time != float('inf'):
        answer = min(answer, sword_time)

    return answer

result = bfs()

if result <= T:
    print(result)
else:
    print("Fail")
