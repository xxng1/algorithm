S = input()

if '::' in S:
    l, r = S.split('::')
    if l:
        left = l.split(':')
    else:
        left = []
    
    if r:
        right = r.split(':')
    else:
        right = []
    
    num = 8 - (len(left) + len(right))
    
    arr = left + ['0000'] * num + right

else:
    arr = S.split(':')

for i in range(len(arr)):
    if len(arr[i]) != 4:
        while(len(arr[i]) != 4):
            arr[i] = '0' + arr[i]



print(':'.join(arr))