import sys

N, X = map(int, sys.stdin.readline().split())
visitors = list(map(int, sys.stdin.readline().split()))

window_sum = sum(visitors[:X])
max_visitors = window_sum
count_max = 1

for i in range(1, N - X + 1):
    window_sum = window_sum - visitors[i - 1] + visitors[i + X - 1]
    
    if window_sum > max_visitors:
        max_visitors = window_sum
        count_max = 1
    elif window_sum == max_visitors:
        count_max += 1

if max_visitors == 0:
    print("SAD")
else:
    print(max_visitors)
    print(count_max)
