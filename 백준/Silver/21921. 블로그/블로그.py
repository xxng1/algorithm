import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

window_sum = sum(visitors[:X])
max_visitors = window_sum
count_max = 1
for i in range(N-X):
    window_sum = window_sum - visitors[i] + visitors[i+X]

    if window_sum > max_visitors:
        max_visitors = window_sum
        count_max = 1
    elif window_sum == max_visitors:
        count_max += 1

if max_visitors == 0:
    print('SAD')
else:
    print(max_visitors)
    print(count_max)