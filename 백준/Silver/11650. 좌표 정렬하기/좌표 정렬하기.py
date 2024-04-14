N = int(input())
arr = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    arr.append([x,y])
    
newarr = sorted(arr, key=lambda x:(x[0],x[1]))
 
for i in newarr:
    print(*i)
