from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N = int(input())

names = list(input().split())
names.sort()

id_names = defaultdict()

for i in range(N):
    id_names[names[i]] = i + 1

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

M = int(input())

for _ in range(M):
    information = list(input().split())
    a = id_names[information[0]]
    b = id_names[information[1]]
    
    graph[b].append(a)
    indegree[a] += 1


queue = deque()
roots = []

# print(id_names)

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
        # roots.append(i)
        roots.append(names[i-1])

children = [ [] for _ in range(N+1)]

while queue:
    curr = queue.popleft()

    for nxt in graph[curr]:
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            queue.append(nxt)
            children[curr].append(names[nxt-1]) # i + 1 해줬으니까, name은 그냥 list

# print(names)
roots.sort()

print(len(roots))
print(*roots)

# print(children)
# print(id_names)

for name in names:
    idx = id_names[name]
    
    child_list = children[idx]
    child_list.sort()


    print(name ,len(child_list), *child_list)