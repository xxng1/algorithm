import sys
input = sys.stdin.readline


A=int(input())
user = []
for _ in range(A):
    age, name = input().split()
    user.append([int(age),name])

result = sorted(user, key=lambda x: x[0])

for i, j in result:
    print(i, j)