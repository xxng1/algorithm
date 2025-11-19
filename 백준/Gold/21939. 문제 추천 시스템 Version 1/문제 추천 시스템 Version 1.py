import heapq
import sys
input = sys.stdin.readline

N = int(input())

problems = {}

min_heap = []
max_heap = []

for _ in range(N):
    p, l = map(int, input().split())
    problems[p] = l
    heapq.heappush(min_heap, (l, p))
    heapq.heappush(max_heap, (-l, -p))

M = int(input())

for _ in range(M):
    command = input().split()

    if command[0] == 'add':
        p = int(command[1])
        l = int(command[2])
        problems[p] = l
        heapq.heappush(min_heap, (l, p))
        heapq.heappush(max_heap, (-l, -p))

    elif command[0] == 'recommend':
        x = int(command[1])

        if x == 1:
            while True:
                l, p = max_heap[0]
                l = -l
                p = -p
                if problems.get(p) == l:
                    print(p)
                    break
                heapq.heappop(max_heap)

        else:
            while True:
                l, p = min_heap[0]
                if problems.get(p) == l:
                    print(p)
                    break
                heapq.heappop(min_heap)

    else:
        p = int(command[1])
        del problems[p]