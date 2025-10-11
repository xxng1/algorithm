N = int(input())

small_jump = [0] * (N+1)
big_jump = [0] * (N+1)

for i in range(1, N):
    a, b = map(int, input().split())
    small_jump[i] = a
    big_jump[i] = b
    
K = int(input())

INF = float('inf')
dp = [[INF]*2 for _ in range(N+1)]

dp[1][0] = 0
dp[1][1] = 0

if N >= 2:
    dp[2][0] = small_jump[1]
    dp[2][1] = small_jump[1]

if N >= 3:
    dp[3][0] = min(dp[2][0] + small_jump[2], dp[1][0] + big_jump[1])
    dp[3][1] = min(dp[2][1] + small_jump[2], dp[1][1] + big_jump[1])

for i in range(4, N+1):
    dp[i][0] = min(dp[i-1][0] + small_jump[i-1], dp[i-2][0] + big_jump[i-2])

for j in range(4, N+1):
    dp[j][1] = min(
        dp[j-1][1] + small_jump[j-1],
        dp[j-2][1] + big_jump[j-2],
        dp[j-3][0] + K
    )

print(min(dp[N][0], dp[N][1]))