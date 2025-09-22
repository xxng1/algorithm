from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_dict = dict(zip(want, number))
    
    
    
    for i in range(len(discount) - 10+1):
        if Counter(discount[i:10+i]) == want_dict:
            answer += 1
        # print(Counter(discount[i:10+i]))
        
        
    
    
    
    
    
    
    return answer