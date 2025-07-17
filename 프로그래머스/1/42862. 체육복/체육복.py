def solution(n, lost, reserve):
    if len(lost) > 1:
        lost.sort()
    if len(reserve) > 1:
        reserve.sort()
    
    
    intersection = list(set(lost) & set(reserve))
    
    for person in intersection:
        lost.remove(person)
        reserve.remove(person)
    
    
    reserve_len = len(reserve)
    p1 = 0
    
    while p1 < len(lost):
        visited = False
        
        for p2 in range(len(reserve)):
            # if lost[p1] in reserve:
            #     reserve.remove(lost[p1])
            #     p1 += 1
            #     visited = True
            #     break

            if ( lost[p1] - 1 ) == reserve[p2]:
                reserve.remove(lost[p1] - 1)
                p1 += 1
                visited = True
                break
            elif ( lost[p1] + 1 ) == reserve[p2]:
                reserve.remove(lost[p1] + 1)
                p1 += 1
                visited = True
                break
                
        if not visited:
            p1 += 1
    
    # print( reserve_len - len(reserve)) # 빌려준사람
    # print( len(lost) - ( reserve_len - len(reserve) ) ) # 빌리지못한사람
    
    
    return n - ( len(lost) - ( reserve_len - len(reserve) ) )