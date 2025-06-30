N, M = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(input()))

def dfs(x, y, before_x, before_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited[x][y] = True

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == arr[x][y]:
                if not ( before_x == nx  and before_y == ny ):
                    if visited[nx][ny] == True:
                        return True
                    else:
                        if dfs(nx, ny, x, y) == True:
                            return True
    return False

check = False

for i in range(N):
    for j in range(M):
        visited = [ [0] * M for _ in range(N) ]
        if dfs(i, j, -1, -1) == True:
            check = True
            break

if check == True:
    print("Yes")
else:
    print("No")