# arr= [
#     [2, 3, -21, -22, -23],
#     [5, 6, -22, -23, -25],
#     [-22, -23, 4, 10, 2]
# ]

# N, M = 3, 5

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

prefix = [[0] * (M + 1) for _ in range(N+1)]

# for i in prefix:
#     print(i)


for i in range(1, N+1):
    for j in range(1, M+1):
        prefix[i][j] = ( arr[i-1][j-1]
                        + prefix[i-1][j]
                        + prefix[i][j-1]
                        - prefix[i-1][j-1])

# for i in prefix:
#     print(i)

# x1, y1 = 1, 0
# x2, y2 = 2, 4

# S = ( prefix[x2+1][y2+1]
#      - prefix[x1][y2+1]
#      - prefix[x2+1][y1]
#      + prefix[x1][y1])

# print(S)


answer = -1e9

for x1 in range(N):
    for x2 in range(x1, N):
        for y1 in range(M):
            for y2 in range(y1, M):
                # print(x1, x2, y1, y2)
                S = ( prefix[x2+1][y2+1]
                        - prefix[x1][y2+1]
                        - prefix[x2+1][y1]
                        + prefix[x1][y1])
                if S > answer:
                    answer = S
print(answer)