def solution(food):
    answer = ''
    for i in range(1, len(food)):
        cnt = food[i] // 2
        
        answer += (str(i) * cnt)
        
    answer += '0'
    
    for i in range(len(food)-1, 0, -1):
        cnt = food[i] // 2
        
        answer += (str(i) * cnt)
    
    # print(answer)
        
    
    
    return answer