import sys
input = sys.stdin.readline

N , M = map(int,input().split())
arr = [0]
dic = {}

for idx in range(1,N+1):
    i = input().rstrip()
    arr.append(i)
    dic[i] = idx



for _ in range(M):
    q = input().rstrip()
    if q.isalpha() :
        print(dic[q])
    elif q.isdigit() :
        print(arr[int(q)])