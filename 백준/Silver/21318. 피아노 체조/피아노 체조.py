import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, (input().split())))
count_arr = [0] * (N-1)

# 감소하는 구간만 1로 체크
count_arr = [0] * (N-1)
for i in range(N - 1):
    if arr[i] > arr[i + 1]:
        count_arr[i] = 1

# print(count_arr)

prefix_sum = [0] * N
aprefix_sum = [0] * N

for i in range(1, N):
    prefix_sum[i] = count_arr[i-1] + prefix_sum[i-1]

T = int(input())

for _ in range(T):
    p1, p2 = map(int, input().split())
    print(prefix_sum[p2-1] - prefix_sum[p1-1])

# for i in range(1, N):
#     aprefix_sum[i] = arr[i-1] + aprefix_sum[i-1]

# print(aprefix_sum)