n, k = map(int, input().split())
p1 = 0
p2 = n
visited = False

while p1 <= p2:
    mid = (p1 + p2) // 2
    value = (mid + 1 ) * ( n - mid + 1)

    if value == k:
        visited = True
        break
    elif value < k:
        p1 = mid + 1
    else:
        p2 = mid - 1

if visited:
    print("YES")
else:
    print("NO")

