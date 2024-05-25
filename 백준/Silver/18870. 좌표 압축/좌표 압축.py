n = int(input())

num = list(map(int, input().split()))

setnum = set(num)
setnum = list(setnum)
setnum.sort()

numdict = {}

for i in range(len(setnum)):
    numdict[setnum[i]] = i

for i in num:
    print(numdict[i], end=' ')