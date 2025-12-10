import sys
input = sys.stdin.readline

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

need = [[True]*N for _ in range(N)]


for k in range(N):
    for i in range(N):
        if i == k:
            continue

        for j in range(N):
            if j == k or i == j:
                continue

            if (graph[i][k] + graph[k][j] < graph[i][j]):
                print(-1)
                exit()
            
            if (graph[i][k] + graph[k][j] == graph[i][j]):
                need[i][j] = False


# print(need)
# print(graph)

answer = 0

for a in range(N):
    for b in range(a+1, N):
        if need[a][b] == True:
            answer += graph[a][b]

print(answer)