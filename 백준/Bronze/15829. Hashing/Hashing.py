L = int(input())
ans = 0
a = input()


for i in range(L):
    ans += (ord(a[i])-96) * (31 ** i)
print(ans % 1234567891)