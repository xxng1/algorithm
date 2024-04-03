N = int(input())
count = 0
main = list((input()))

for i in range(N-1):
    compare = input()
    copy = main[:]
    cnt = 0
    for word in compare:        
        if word in copy:
            copy.remove(word)
        else:
            cnt += 1
    
    if cnt < 2 and len(copy) < 2:
        count += 1
print(count)