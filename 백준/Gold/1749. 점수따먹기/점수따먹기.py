import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

def get_max_sum(row):
    cur, best = row[0], row[0]
    for x in row[1:]:
        cur = max(x, cur + x)
        best = max(cur, best)
    return best

ans = -1e9
for start in range(n):
    temp = [0] * m
    for i in range(start, n):
        row = arr[i]
        for j in range(m):
            temp[j] += row[j]
        cur_max = get_max_sum(temp)
        ans = max(ans, cur_max)
print(ans)

# print(temp)