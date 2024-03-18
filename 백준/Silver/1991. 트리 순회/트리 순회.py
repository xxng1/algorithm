import sys
input = sys.stdin.readline

N = int(input())
tree = {}

for i in range(N):
    a, b, c = list(map(str, input().split()))
    tree[a] = [b, c]

def front(root):
    if root != '.':
        print(root, end='')
        front(tree[root][0])
        front(tree[root][1])

def mid(root):
    if root != '.':
        mid(tree[root][0])
        print(root, end='')
        mid(tree[root][1])

def last(root):
    if root != '.':
        last(tree[root][0])
        last(tree[root][1])
        print(root, end='')

front('A')
print()
mid('A')
print()
last('A')
print()