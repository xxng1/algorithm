import sys

A, B, C = list((sys.stdin.readline().split()))

A = list(map(int, A.split(':')))
A = A[0] * 60 + A[1]

B = list(map(int, B.split(':')))
B = B[0] * 60 + B[1]

C = list(map(int, C.split(':')))
C = C[0] * 60 + C[1]

dct = {}

while True:
    chat = sys.stdin.readline().rstrip()
    
    if chat == '':
        break
    
    time, person = chat.split(' ')
    hour, minute = list(map(int, time.split(':')))
    
    sum_minute = hour * 60 + minute

    # print('----', hour, minute,'----')
    if sum_minute <= A:
        # print(person, 'AAAAA')
        dct[person] = 1

    if ( B <= sum_minute <= C):
        if person in dct:
            dct[person] = 10

        # print(person, 'BBBBB')
    
    # print('--------')
    
cnt = 0
for i in dct.values():
    if i == 10:
        cnt += 1

print(cnt)

# print(dct)


# < A[0] A[1] 
# < B[0] B[1]
# C[0] C[1] 
