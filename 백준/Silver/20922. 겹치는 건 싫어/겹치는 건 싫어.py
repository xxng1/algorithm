N, K = map(int, input().split())
arr = list(map(int, input().split()))

element_count = {}
max_length = 0
start = 0

for end in range(N):
    # end 포인터가 가리키는 원소의 개수를 증가
    if arr[end] in element_count:
        element_count[arr[end]] += 1
    else:
        element_count[arr[end]] = 1

    # K를 초과하는 경우 start 포인터를 이동
    while element_count[arr[end]] > K:
        element_count[arr[start]] -= 1
        if element_count[arr[start]] == 0:
            del element_count[arr[start]]
        start += 1

    # 최대 길이 갱신
    max_length = max(max_length, end - start + 1)

print(max_length)