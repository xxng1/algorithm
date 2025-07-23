from collections import deque


def solution(prices):
    
    answer = []
    
    queue = deque(prices)
    
    # print(queue)
    
    while queue:
        tmp = queue.popleft()
        
        period = 0
        for check in queue:
            period += 1
            if tmp <= check:
                continue
            else:
                break
        
        answer.append(period)
        
    
    return answer