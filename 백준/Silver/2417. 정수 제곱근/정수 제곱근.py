n = int(input())

left = 0
right = n
while(left<= right):
    mid = (left+right)//2
    if mid ** 2 >= n:
        right = mid -1
    else:
        left = mid + 1
print(left)