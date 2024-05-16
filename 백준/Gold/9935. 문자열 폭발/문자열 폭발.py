import sys
input = sys.stdin.readline

N = list(sys.stdin.readline().rstrip())
a = list(sys.stdin.readline().rstrip())

stack = []

for i in N:
    stack.append(i)
    if stack[len(stack) - len(a):len(stack)] == a:
        for _ in range(len(a)):
            stack.pop()
    

if stack:
    print(*stack, sep='')
else:
    print("FRULA")
