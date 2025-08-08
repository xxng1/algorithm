import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())

arr = []

for _ in range(M):
    arr.append(list(map(int, input().split())))

graph = [ [] for _ in range(N+1) ]
# print(graph)

indegree = [0] * (N+1)

queue = deque()

for i in range(len(arr)):
    checklist = arr[i][1:]
    # print(checklist)
    for j in range(len(checklist)-1):
        # print(checklist[j:j+2])
        a = checklist[j]
        b = checklist[j+1]
        graph[a].append(b)
        indegree[b] += 1

    # print('asd',graph)
    # print(indegree)

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

# print(queue)

answer = []

while queue:
    now = queue.popleft()
    answer.append(now)
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

if len(answer) != N:
    print(0)
else:
    for i in answer:
        print(i)