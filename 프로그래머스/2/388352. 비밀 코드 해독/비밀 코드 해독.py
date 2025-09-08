from itertools import combinations


def solution(n, q, ans):
    answer = 0
    # checklen = len(q[0])
    
    # checklist = deque()
    
    numlist = [ i for i in range(1, n+1)]
    
    asd = list(combinations(numlist, 5))
    
    cnt = 0
    
    
    
    for check_numlist in asd:
        flag = False
        for i in range(len(q)):
            checkpoint = len(set(check_numlist) & set(q[i]))
            if ans[i] != checkpoint:
                flag = False
                break
            else:
                flag = True
        if flag:
            # print(check_numlist)
            cnt += 1
            
    # print(cnt)
    
    qwe = set([3,4,7,9,10]) & set([2,5,7,9,10])
    # print(len(qwe))
    
    
    return cnt