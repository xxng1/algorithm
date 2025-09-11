from collections import deque

def bfs(y, x, land, visited):
    n = len(land)
    m = len(land[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((y, x))
    visited.add((y, x))

    area_size = 0
    cols = set()  # 이 영역이 차지하는 열들

    while queue:
        cy, cx = queue.popleft()
        area_size += 1
        cols.add(cx)

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if land[ny][nx] == 1 and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    queue.append((ny, nx))

    return area_size, cols


def solution(land):
    n = len(land)
    m = len(land[0])

    visited = set()
    col_sums = [0] * m  # 각 열에 대해 최대 유량 합산

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and (i, j) not in visited:
                area_size, cols = bfs(i, j, land, visited)
                for c in cols:
                    col_sums[c] += area_size

    return max(col_sums)
