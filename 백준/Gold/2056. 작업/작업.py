from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

works = [ [] for _ in range(N+1) ]
indegree = [0] * (N+1)
dp = [0] * (N+1)
costs = [0] * (N+1)

for i in range(1, N+1):
    s = list(map(int, input().split()))
    
    costs[i] = s[0]

    if s[1] != 0:
        for num in range(2, len(s)):
            works[s[num]].append(i)
            indegree[i] += 1


queue = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = costs[i]

while queue:
    tmp = queue.popleft()

    for next in works[tmp]:
        indegree[next] -= 1
        dp[next] = max(dp[next], dp[tmp] + costs[next])

        if indegree[next] == 0:
            queue.append(next)


print(max(dp))
# print(dp)
# print(indegree)