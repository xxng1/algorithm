def count_valid_parentheses(N):
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]

    return dp[N]

while(True):
    N = int(input())
    if N == 0:
        break
    print(count_valid_parentheses(N))
