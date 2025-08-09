
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
cost = [0] * (N + 1)
dp = [0] * (N + 1)

for build in range(1, N + 1):
    s = list(map(int, input().split()))
    cost[build] = s[0]
    for pre in s[1:-1]:
        graph[pre].append(build)
        indegree[build] += 1


queue = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = cost[i]


# print(queue)
# dp = [0] * (N + 1)
# answer = []
while queue:
    now = queue.popleft()
    # answer.append(now)

    for next in graph[now]:
        indegree[next] -= 1
        dp[next] = max(dp[next], dp[now] + cost[next])
        if indegree[next] == 0:
            queue.append(next)




for i in range(1, N+1):
    print(dp[i])
    