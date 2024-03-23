import sys
input = sys.stdin.readline
from collections import deque

n,m,k,x=map(int,input().split())

g=[[] for i in range(n+1)]#n+1개의 노드를 갖는 그래프 생성

for i in range(m):#도로 입력받기
    a,b=map(int,input().split())
    g[a].append(b)

d=[-1]*(n+1)#노드 간 거리 -1로 초기화
d[x]=0#시작 노드의 거리는 0으로

queue = deque([x])
while queue:
    v = queue.popleft()
    for i in (g[v]):
        if d[i] == -1:
            d[i] = d[v] + 1
            queue.append(i)

tf = False

for i in range(1,n+1):
    if d[i] == k:
        print(i)
        tf = True

if tf == False:
    print(-1)