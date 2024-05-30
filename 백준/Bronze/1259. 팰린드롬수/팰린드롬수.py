t = input()

while t != '0':
    arr1 = []
    arr2 = []
    for i in range(0, len(t)):
        arr1.append(t[i])
    for i in range(len(t), 0, -1):
        arr2.append(t[i-1])
    if arr1 == arr2:
        print('yes')
    else:
        print('no')
    
    t = input()
