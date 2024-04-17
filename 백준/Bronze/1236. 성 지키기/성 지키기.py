N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
row_arr = [1 for _ in range(N)]
col_arr = [1 for _ in range(M)]
for row in range(N):
    if 'X' in graph[row]:
        row_arr[row] = 0
for col in range(M):
    k = [graph[row][col] for row in range(N)]
    if 'X' in k:
        col_arr[col] = 0
print(max(sum(row_arr),sum(col_arr)))