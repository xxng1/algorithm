N, M = map(int, input().split())
dict_1 = {}
for _ in range(N):
    a, b = map(str, input().split())
    dict_1[a] = b

for _ in range(M):
    a = input()
    print(dict_1[a])