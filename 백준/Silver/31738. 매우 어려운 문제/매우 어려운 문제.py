N, M = map(int, input().split())

if N >= M:
    print(0)
else:
    result = 1
    for i in range(1, N+1):
        result = (result * i) % M
    print(result)
