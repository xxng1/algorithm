import sys
input = sys.stdin.readline

N = int(input())

arr = set()

for i in range(N):
    todo = list(input().split())
    
    if todo[0] == 'add':
        arr.add(int(todo[1]))

    elif todo[0] == 'remove':
        try:
            arr.remove(int(todo[1]))
        except:
            pass
        
    elif todo[0] == 'check':
        if int(todo[1]) in arr:
            print(1)
        else:
            print(0)
    
    elif todo[0] == 'toggle':
        if int(todo[1]) in arr:
            arr.remove(int(todo[1]))
        else:
            arr.add(int(todo[1]))
        
    elif todo[0] == 'all':
        arr = set([i for i in range(1,21)])
        
    elif todo[0] == 'empty':
        arr.clear()