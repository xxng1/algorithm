N = int(input())

arr = []

for i in range(N):
    arr.append(list(input().split('.')))

# print("---")
# print(arr)

arr.sort(key = lambda x:x[1])

# print(arr)
# print("---")

dict = {}

for a, b in arr:
    if b in dict:
        dict[b] += 1
    else:
        dict[b] = 1

# print(dict)

for x, y in dict.items():
    print(x, y)