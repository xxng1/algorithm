# 1 = 1
# 2 = 2
# 3 = 1 + 2 = 3
# 4 = 1 + 3 + 1 = 5
# 5 = 1 + 4 + 3 = 8
# 6 = 1 + 5 + 5 + 1 + 2  = 13

n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n]%10007)