N = int(input())
score = []

for _ in range(N):
    score.append(int(input()))

dp = [0] * (N+1)
dp[1] = score[0]
if N > 1:
    dp[2] = score[0] + score[1]
if N > 2:
    dp[3] = max(score[0] + score[2], score[1] + score[2])

for i in range(4, N+1):
    dp[i] = max(dp[i-2]+score[i-1], dp[i-3]+score[i-2]+score[i-1])

print(dp[N])
