import sys

input = sys.stdin.readline

T = int(input())
arr0 = [0] * 45
arr1 = [0] * 45

arr0[0] = 1
arr1[0] = 0
arr0[1] = 0
arr1[1] = 1

for i in range(2, 42):
    arr0[i] = arr0[i - 1] + arr0[i - 2]
    arr1[i] = arr1[i - 1] + arr1[i - 2]

for _ in range(T):
    n = int(input())
    print(arr0[n], arr1[n])