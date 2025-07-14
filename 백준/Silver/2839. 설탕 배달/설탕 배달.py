N = int(input())

dp = [0] * (N + 1)

if N < 5:
    dp[3] = 1
else:
    dp[3] = dp[5] = 1

for i in range(6, N+1):
    a = dp[i-3]
    b = dp[i-5]

    if a != 0 and b != 0:
        dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)
    elif a != 0:
        dp[i] = dp[i-3] + 1
    elif b != 0:
        dp[i] = dp[i-5] + 1


if dp[N] == 0:
    print(-1)
else:
    print(dp[N])        