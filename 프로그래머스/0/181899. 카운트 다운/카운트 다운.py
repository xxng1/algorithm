def solution(start, end_num):
    answer = []
    N = start - end_num
    for i in range(N+1):
        answer.append(start-i)
    
    
    return answer