N, M = map(int, input().split())

count = 0
S = set()

for _ in range(N):
    S.add(input())

for _ in range(M):
    tmp = input()
    if tmp in S:
        count += 1

print(count)