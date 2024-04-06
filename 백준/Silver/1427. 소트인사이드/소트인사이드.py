N = input()
A = []
for i in N:
    A.append(int(i))
    
A.sort(reverse=True)
for i in A:
    print(i, end='')