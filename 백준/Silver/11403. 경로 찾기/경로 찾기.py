import sys
input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))


# list[l][j] = min(list[i][j], list[i][k] + list[k][j])

for k in range(n):
    for i in range(n):
        for j in range(n):
            # graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for i in graph:
    print(*i)