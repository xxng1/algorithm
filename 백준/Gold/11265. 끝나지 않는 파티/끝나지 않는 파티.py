import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))


# graph = [[0, 4, 4, 8, 7], [7, 0, 7, 7, 4], [1, 4, 0, 5, 4], [5, 2, 2, 0, 7], [1, 4, 1, 6, 0]]
for k in range(N):
    for i in range(N):
        # if i == k:
        #     continue
        
        for j in range(N):
            # if k == j or i == j:
            #     continue
            
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


# for i in graph:
#     print(i)

for _ in range(M):
    a, b, c = map(int,input().split())
    if graph[a-1][b-1] > c:
        print("Stay here")
    else:
        print("Enjoy other party")