def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a
        return True
    return False


N = int(input())

edges = []
parent = [i for i in range(N)]

arr = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    for j in range(i + 1 , N ):
        edges.append((arr[i][j], i, j))

edges.sort()


answer = 0
cnt = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer += cost
        cnt += 1

        if cnt == N - 1:
            break


print(answer)