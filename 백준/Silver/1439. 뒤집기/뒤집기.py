
s = input()
a = 0
b = 0
p = s[0]

if p == '1':
    b += 1
else:
    a += 1

for i in range(len(s)):
    if p == s[i]:
        continue
    else:
        p = s[i]
        if s[i] == '1':
            b += 1
        else:
            a += 1

print(min(a, b))