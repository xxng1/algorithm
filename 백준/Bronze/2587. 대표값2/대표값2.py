arr = []
for i in range(5):
    arr.append(int(input()))
    
print(int(sum(arr)/len(arr)))
print(sorted(arr)[2])