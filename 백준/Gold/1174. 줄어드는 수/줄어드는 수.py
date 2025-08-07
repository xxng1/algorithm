N = int(input())
answer = []

def backtracking(cur):
    answer.append(int(cur))
    for i in range(0, int(cur[-1])):
        backtracking(cur + str(i))
        
for i in range(10):
    backtracking(str(i))

answer.sort()

# print(answer[N])
# print(N)
# print(len(answer))
# print(answer[-1])
# print(len(answer))

if N > 1023:
    print(-1)
else:
    print(answer[N-1])

# if N > 1022:
#     print(-1)
# else:
#     print(answer[N])        