import sys
input = sys.stdin.readline


N, K = map(int, input().split())

graph = []


for _ in range(N):
    command = list(map(int, input().split()))
    graph.append(command)


# print(graph)


for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]



result = float('inf')
visited = [0] * N
visited[K] = 1

def bt(start, depth, ans):
    global result

    if depth == N:
        result = min(result, ans)
        return visited
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            bt(i, depth + 1, ans + graph[start][i])
            visited[i] = 0

bt(K, 1, 0)

print(result)

# print(visited)
# print(graph)
