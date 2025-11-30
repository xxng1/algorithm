import sys
input = sys.stdin.readline

n = int(input())
graph = [ [float('inf')] * (n) for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

m = int(input())

for _ in range(m):
    v, u, w = map(int, input().split())
    graph[v-1][u-1] = min(graph[v-1][u-1], w)


# for i in graph:
#     print(i)


for k in range(n):
    for i in range(n):
        for j in range(n):
            if (graph[i][k] != float('inf') and graph[k][j] != float('inf')):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in graph:
    for j in i:
        if j == float('inf'):
            print(0, end = ' ')
        else:
            print(j, end = ' ')
    print()