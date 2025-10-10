import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)


V, E = map(int, input().split())

edges = []

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    
    return parent[x]

def union_find(a, b):
    a = get_parent(a)
    b = get_parent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a, b):
    return get_parent(a) == get_parent(b) 


for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


edges.sort(key=lambda x : x[2])

parent = [ i for i in range( V + 1)]


answer = 0
for a, b, cost in edges:
    if not same_parent(a,b):
        union_find(a, b)
        answer += cost
print(answer)
