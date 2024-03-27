N = int(input())
M = int(input())
my_list = list(map(int, input().split()))

my_list.sort()
start, end = 0, len(my_list)-1
cnt = 0 

while start < end: 
    result = my_list[start] + my_list[end]
    if result > M:
        end -= 1 
    elif result < M:
        start += 1
    else:
        cnt   += 1 
        start += 1 
        end   -= 1 

print(cnt)