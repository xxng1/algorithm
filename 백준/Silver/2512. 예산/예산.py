N = int(input())
arr = list(map(int, input().split()))
M = int(input())

start = 0
end = max(arr)

while(start<=end):
    mid = (start+end)//2
    
    total = 0

    for i in range(len(arr)):
        if arr[i] < mid:
            total += arr[i]
        else:
            total += mid
    
    if total <= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
        
        
    