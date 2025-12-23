from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    score = list(map(int, input().split()))

    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N + 1)
    queue = deque()

    for i in range(N-1):
        for j in range(i+1, N):
            graph[score[i]].append(score[j])
            indegree[score[j]] += 1


    M = int(input())

    for _ in range(M):
        a, b = map(int, input().split())
        flag = True

        for check in graph[a]:
            if check == b:
                graph[a].remove(b)
                graph[b].append(a)

                indegree[b] -= 1
                indegree[a] += 1

                flag = False
        
        if flag:
            graph[b].remove(a)
            graph[a].append(b)

            indegree[b] += 1
            indegree[a] -= 1

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    answer = []
    question_mark = False
    

    if not queue:
        print("IMPOSSIBLE")
        continue


    while queue:
        if len(queue)> 1:
            question_mark = True


        curr = queue.popleft()
        answer.append(curr)

        for nxt in graph[curr]:
            indegree[nxt] -= 1
            
            if indegree[nxt] == 0:
                queue.append(nxt)



    if len(answer) < N:
        print("IMPOSSIBLE")
    elif question_mark:
        print("?")
    else:
        print(*answer)