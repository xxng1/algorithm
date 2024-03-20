import sys
input = sys.stdin.readline

N = int(input())
arrN = list(map(int, input().split()))
M = int(input())
arrM = list(map(int, input().split()))

arrN.sort()

ans = [0] * M
for i in range(M):
    left = 0
    right = N-1
    while(left <= right):
        mid = (left+right)//2
        if(arrM[i]==arrN[mid]):
            ans[i] = 1
            break
        elif(arrM[i]<arrN[mid]):
            right = mid - 1
        else:
            left = mid + 1

for i in ans:
    print(i)