def solution(n, lost, reserve):
    if len(lost) > 1:
        lost.sort()
    if len(reserve) > 1:
        reserve.sort()
    
    # ✅ 교집합 제거
    intersection = list(set(lost) & set(reserve))
    for person in intersection:
        lost.remove(person)
        reserve.remove(person)

    reserve_len = len(reserve)
    p1 = 0
    
    while p1 < len(lost):
        visited = False
        
        for p2 in range(len(reserve)):
            if (lost[p1] - 1) == reserve[p2] or (lost[p1] + 1) == reserve[p2]:
                reserve.pop(p2)
                visited = True
                break
        
        if visited:
            lost.pop(p1)
        else:
            p1 += 1
    
    return n - len(lost)
