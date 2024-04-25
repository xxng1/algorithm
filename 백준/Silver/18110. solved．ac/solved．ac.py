import sys
input = sys.stdin.readline

n = int(input())

arr = []

def func(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


if n == 0:
    print(0)
    exit()
else:
    for i in range(n):
        arr.append(int(input()))

arr.sort()

p = func(n * 0.15)
summ = 0

for i in range(p, n-p):
    summ += arr[i]

print(func(summ /( n-p - p)))