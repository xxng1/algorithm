# import sys
# input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

# prefix_sum = 0
prefix_sum = [0] * n
remain_arr = [0] * m
result = 0
for i in range(n):
    prefix_sum[i] += prefix_sum[i-1] + arr[i]
    remain = prefix_sum[i] % m
    # print(remain)
    if remain == 0:
        result += 1
    
    remain_arr[remain] += 1

# print(prefix_sum)
# print(remain_arr)

for i in range(m):
    tmp = remain_arr[i]
    if tmp != 0:
        result += ((tmp) * (tmp - 1)) // 2
print(result)
        