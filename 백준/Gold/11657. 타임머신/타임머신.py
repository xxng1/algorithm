import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graph = []
INF = float('inf')
dp = [INF] * (N+1)

for _ in range(M):
    graph.append(list(map(int, input().split())))



def bellmanford(start):
    dp[start] = 0

    for i in range(1, N+1):
        for j in range(M):
            curr, nxt, cost = graph[j][0], graph[j][1], graph[j][2]

            if dp[curr] != INF and dp[nxt] > dp[curr] + cost:
                dp[nxt] = dp[curr] + cost
            
                if i == N:
                    return True
    return False


chk = bellmanford(1)

# print(chk)
# print(dp)


if chk:
    print(-1)
else:
    for output in range(2, N+1):
        if dp[output] == INF:
            print(-1)
        else:
            print(dp[output])


    