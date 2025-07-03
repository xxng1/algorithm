N = int(input())
graph = []

for i in range(N):
    graph.append(list((input())))

visited = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0

def dfs(x, y):
    global count
    visited[x][y] = True

    if graph[x][y] == '0':
        return

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == False:
                if graph[nx][ny] == '1':
                    # visited[nx][ny] = True
                    count += 1
                    dfs(nx, ny)
    


answer = []
cnt = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and visited[i][j] == 0:
            count = 1
            dfs(i, j) 
            if count != 0:
                cnt += 1
                answer.append(count)

answer.sort()
print(cnt)
for i in answer:
    print(i)