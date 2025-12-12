import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

L0 = [0] * N
L1 = [0] * N

if A[0] == 0:
    L0[0] = 1
else:
    L1[0] = 1

for i in range(1, N):
    if A[i] == 0:
        L0[i] = L0[i-1] + 1
    else:
        L1[i] = L1[i-1] + 1

R0 = [0] * N
R1 = [0] * N

if A[N-1] == 0:
    R0[N-1] = 1
else:
    R1[N-1] = 1

for i in range(N-2, -1, -1):
    if A[i] == 0:
        R0[i] = R0[i+1] + 1
    else:
        R1[i] = R1[i+1] + 1


answer = max(max(L0), max(L1))


for X in range(N):
    flipped = 1 - A[X]

    if A[X] == 0:
        left_run = L0[X]
    else:
        left_run = L1[X]

    if X+1 < N:
        if flipped == A[X+1]:
            if flipped == 0:
                answer = max(answer, left_run + R0[X+1])
            else:
                answer = max(answer, left_run + R1[X+1])
        else:
            answer = max(answer, left_run)
    else:
        answer = max(answer, left_run)

print(answer)