import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

arr = [[] for _ in range(N+1) ]
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (N+1)
parent = [0] * (N+1)

def dfs(start):
    visited[start] = True
    for i in arr[start]:
        if not visited[i]:
            parent[i] = start
            dfs(i)

dfs(1)

for i in range(2, N+1):
    print(parent[i])


