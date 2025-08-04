from collections import deque
import sys

input = sys.stdin.readline

n, l, r = map(int,input().split())
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))


def bfs(x, y, graph, visited):
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    union = deque()

    queue.append((x, y))
    union.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False:
                    checkpoint = abs(graph[nx][ny] - graph[x][y])
                    if l <= checkpoint <= r:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        union.append((nx, ny))
    
    return union

total_migrate = 0

while True:
    
    # count_zero = 0 # n * n 이면 break. 이동 x.
    # count_migrate = 0

    is_moved = False

    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):

            if not visited[i][j]:
                check = bfs(i, j, graph, visited)
            

                if len(check) > 1:
                    is_moved = True
                    graph_sum = 0
                    for graph_count in check:
                        x = graph_count[0]
                        y = graph_count[1]
                        
                        graph_sum += graph[x][y]
                    
                    
                    for graph_count in check:
                        x = graph_count[0]
                        y = graph_count[1]

                        graph[x][y] = graph_sum // len(check)
    
    if not is_moved:
        break
    else:
        total_migrate += 1

print(total_migrate)
# print(graph)



# print(graph)

# print('---')

# count_zero = 0 # n * n 이면 break. 이동 x.
# count_migrate = 0


# visited = [[False]*n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         check = bfs(i, j, graph)

#         if len(check) == 1:
#             count_zero += 1                

#         else:
#             count_migrate += 1
#             graph_sum = 0
#             for graph_count in check:
#                 x = graph_count[0]
#                 y = graph_count[1]
                
#                 graph_sum += graph[x][y]
            
            
#             for graph_count in check:
#                 x = graph_count[0]
#                 y = graph_count[1]

#                 graph[x][y] = graph_sum // len(check)

# print(count_zero)
# print(count_migrate)

# print(graph)

# print('---')


# count_zero = 0 # n * n 이면 break. 이동 x.
# count_migrate = 0

# visited = [[False]*n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         check = bfs(i, j, graph)

#         if len(check) == 1:
#             count_zero += 1                

#         else:
#             count_migrate += 1
#             graph_sum = 0
#             for graph_count in check:
#                 x = graph_count[0]
#                 y = graph_count[1]
                
#                 graph_sum += graph[x][y]
            
            
#             for graph_count in check:
#                 x = graph_count[0]
#                 y = graph_count[1]

#                 graph[x][y] = graph_sum // len(check)

# print(count_zero)
# print(count_migrate)

# print(graph)

# print('---')