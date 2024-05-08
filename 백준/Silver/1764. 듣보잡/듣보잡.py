N, M = map(int, input().split())

arr_1 = set()
arr_2 = set()

for _ in range(N):
    arr_1.add(input())

for _ in range(M):
    arr_2.add(input())


count = 0
checklist = []
for i in arr_1:
    if i in arr_2:
        count += 1
        checklist.append(i)

print(count)

for i in sorted(checklist):
    print(i)