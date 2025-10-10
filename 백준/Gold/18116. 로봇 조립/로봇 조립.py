import sys
input = sys.stdin.readline

n = int(input())

parent = [i for i in range(1000001)]
size = [1] * ( 1000001 )


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return
    elif a > b:
        parent[a] = b
        size[b] += size[a]
    else:
        parent[b] = a
        size[a] += size[b]

for _ in range(n):
    S = input().split()
    if S[0] == 'I':
        union(int(S[1]), int(S[2]))
    else:
        x = int(S[1])
        print(size[find(x)])
        
        