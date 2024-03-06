N = int(input())

cache = [0] * 11

cache[1] = 1
cache[2] = 2
cache[3] = 4

for i in range(4, 11):
    cache[i] = sum(cache[i-3:i])

for i in range(N):
    num = int(input())
    print(cache[num])