import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[1e9] * (N) for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    if c == 0:
        # graph[a].append(b)
        graph[a-1][b-1] = 0
        graph[b-1][a-1] = 1
    elif c == 1:
        # graph[a].append(b)
        # graph[b].append(a)
        graph[a-1][b-1] = 0
        graph[b-1][a-1] = 0

for i in range(N):
     graph[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
                # graph[i][j] = max(graph[i][j], graph[i][k] + graph[k][j])
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


# for i in graph:
#     print(i)

K = int(input())

for _ in range(K):
     s, e = map(int, input().split())
     print(graph[s-1][e-1])