from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())

    arr = [[] for _ in range(N+1)]
    costs = [0] + list(map(int, input().split()))

    dp = [0] * (N + 1)
    indegree = [0] * (N + 1)

    for _ in range(K):
        a, b = map(int, input().split())
        arr[a].append(b)
        indegree[b] += 1

    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = costs[i]

    answer = []
    now = [0]
    result = costs[0]

    while queue:
        tmp = queue.popleft()
        # answer.append(tmp)

        # now = [0]
        for i in arr[tmp]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[tmp] + costs[i])

            if indegree[i] == 0:
                queue.append(i)
                # now.append(costs[i-1])
    # print(dp)
    W = int(input())
    print(dp[W])