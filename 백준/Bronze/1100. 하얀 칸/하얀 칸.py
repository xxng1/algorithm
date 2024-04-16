a = ""
for i in range(4):
    a += input()[::2]
    a += input()[1::2]
print(a.count("F"))