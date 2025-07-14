# import sys
# input = sys.stdin.readline

def palindrome(p1, p2, arr):
    while p1 < p2:
        if arr[p1] == arr[p2]:
            p1 += 1
            p2 -= 1
        else:
            return False
    return True
    


T = int(input())

for _ in range(T):
    S = input()

    p1 = 0
    p2 = len(S) - 1


    check_pal = 0
    
    # print(palindrome(p1, p2, S))
    while p1 < p2:
        if S[p1] == S[p2]:
            p1 += 1
            p2 -= 1
        else:
            if check_pal == 0:
                if palindrome(p1+1, p2, S) == True:
                    check_pal = 1
                    break
                elif palindrome(p1, p2-1, S) == True:
                    check_pal = 1
                    break
                else:
                    check_pal = 2
                    break
            else:
                check_pal = 2
                break                
    
    print(check_pal)