#2를 곱했는데 1이되는경우는 없음 거꾸로내려오면 될듯

A, B = (input().split())

cnt = 1
while True:
    if A == B:
        break

    if int(B) < int(A):
        cnt = -1
        break
    elif B[-1] == '1':
        B = B[0:-1]
        cnt += 1
    elif int(B) % 2 != 0:
        cnt = -1
        break
    else:
        B = str(int(B) // 2)
        cnt += 1

print(cnt)