
T = int(input())

for _ in range(T):
    n = int(input())
    dict = {}
    for _ in range(n):
        a, b = input().split()
        if dict.get(b) == None:
            dict[b] = set()
        dict[b].add(a)

        
    result = 1

    for i in dict.keys():
        result *= len(dict[i]) + 1
        
    print(result-1)