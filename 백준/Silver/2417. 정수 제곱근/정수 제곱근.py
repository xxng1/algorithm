N = int(input())

p1 = 0
p2 = N



while p1 <= p2:
    mid = (p1 + p2) // 2

    if (mid) * (mid) >= N:
        p2 = mid -1
    else:
        p1 = mid + 1 

print(p1)
