N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
sum = 0
cnt = 0

while True:
    if sum >= M:
        sum -= arr[start]
        start += 1
    elif end == N:
        break
    else:
        sum += arr[end]
        end += 1
    if sum == M:
        cnt += 1

print(cnt)
