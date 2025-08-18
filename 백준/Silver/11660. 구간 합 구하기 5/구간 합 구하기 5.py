import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

prefix = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] = - prefix[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] + arr[i-1][j-1]
        
        
for i in range(M):
    x1, x2, y1, y2 = map(int, input().split())
    
    result = prefix[y1][y2] - prefix[x1-1][y2] - prefix[y1][x2-1] + prefix[x1-1][x2-1]
    print(result)        
