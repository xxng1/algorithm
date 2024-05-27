from collections import deque

N, K = map(int, input().split())
MAX = 10 ** 5
graph = [0] * (MAX + 1)

def bfs(x):
    queue = deque()
    queue.append(x)
    dx = [-1, 1, 2]

    while queue:
        x = queue.popleft()
        if x == K:
            break
        for i in range(3):
            if i == 2:
                nx = x * dx[i]
            else:
                nx = x + dx[i]
            
            if 0 <= nx <= MAX and not graph[nx]:
                graph[nx] = graph[x] + 1
                queue.append(nx)

bfs(N)
print(graph[K])