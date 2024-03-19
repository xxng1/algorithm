import sys
input = sys.stdin.readline


N = int(input())
milk = []
for _ in range(N):
    milk.append(int(input()))

milk.sort(reverse=True)
for i in range(1, N):
    if (i+1) % 3 == 0:
        milk[i] = 0

print(sum(milk))
