import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

prefix = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix[i][j] = (
            arr[i - 1][j - 1]+ prefix[i - 1][j]+ prefix[i][j - 1]- prefix[i - 1][j - 1]
        )

T = int(input())
for i in range(T):
    x1, x2, y1, y2 = map(int, input().split())
    result = prefix[y1][y2] - prefix[y1][x2-1] - prefix[x1-1][y2] + prefix[x1 -1][x2 -1]
    print(result)