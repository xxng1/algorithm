n = input()
f = int(input())

start = int(n[:-2] + '00')
end = int(n[:-2] + '99')

num = 0

for i in range(start, end + 1):
    if i % f == 0:
        num = i
        break
    
print(str(num)[-2:])