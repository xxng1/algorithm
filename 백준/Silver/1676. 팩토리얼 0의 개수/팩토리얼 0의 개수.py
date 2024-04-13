import sys
from math import factorial

input = sys.stdin.readline

N = int(input())

# def factorial(num):
#     if num == 1 or num == 2:
#         return num
#     else:
#         return num * factorial(num-1)
    
S = str(factorial(N))

count = 0

for i in range(len(S)):
    if S[len(S)-1-i] == '0':
        count += 1
    else:
        break

print(count)