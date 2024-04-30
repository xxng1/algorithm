N = int(input())

arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))
    
newarr = sorted(arr, key = lambda x: x[0])
newarr = sorted(newarr, key = lambda x: x[1])

cnt = 1
end = newarr[0][1]
for i in range(1, N):
    if end <= newarr[i][0]:
        end = newarr[i][1]
        cnt += 1
        
print(cnt)