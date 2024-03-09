import sys

N, M = map(int, sys.stdin.readline().split())

arr = [0] * 10
visited = [0] * 10

def func(cnt, start):
    if(cnt == M):
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return
    
    for i in range(start, N):
        # if (visited[i]):
        arr[cnt] = i+1
        visited[i] = 1
        func(cnt+1, i)
        visited[i] = 0

func(0, 0)
