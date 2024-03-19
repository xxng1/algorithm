import sys
input = sys.stdin.readline

N = int(input())

li = list(map(int, input().split()))


dp1 = [1] * N
dp2 = [1] * N

for i in range(N-1):
    if li[i] <= li[i+1]:
        dp1[i+1] = dp1[i]+1
    
for i in range(N-1):
    if li[i] >= li[i+1]:
        dp2[i+1] = dp2[i]+1

print(max(dp1) if max(dp1)>max(dp2) else max(dp2))
