N = int(input())
arr = list(map(int, input().split()))

p1 = 0
p2 = len(arr)-1
arr.sort()

abs_zero = abs(arr[p1] + arr[p2])
ans = (arr[p1], arr[p2])

while p1 < p2 :
    result = arr[p1] + arr[p2]

    if abs(result) < abs_zero:
        abs_zero = abs(result)
        ans = (arr[p1], arr[p2])
    
    if result == 0:
        break
    elif result < 0:
        p1 += 1
    elif result > 0:
        p2 -= 1

print(*sorted(ans))