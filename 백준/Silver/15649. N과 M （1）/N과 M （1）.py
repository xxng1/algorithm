N, M = map(int, input().split())

arr = [0] * 10
visited = [0] * 10

def func(cnt):
    if(cnt == M):
        for i in range(M):
            print(arr[i], end=' ')
        print()
    
    
    for i in range(N):
        if not(visited[i]):
            arr[cnt] = i+1
            visited[i] = 1
            func(cnt+1)
            visited[i] = 0

func(0)

