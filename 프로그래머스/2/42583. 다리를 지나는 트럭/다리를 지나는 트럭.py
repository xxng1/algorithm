from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    queue = deque(truck_weights)
    bridge_list = deque([0 for _ in range(bridge_length)])
    
    # print(queue)
    # print(bridge_list)
    # asd = deque([1,3,5])
    # print(sum(asd))
    cnt = 0
    sum_var = 0
    
    while queue: # 다 타기까지
        cnt += 1
        
        truck = queue.popleft()
        sum_var_tmp = bridge_list.popleft()
        
        sum_var -= sum_var_tmp
        
        # if truck + sum(bridge_list) > weight:
        if truck + sum_var > weight:            
            queue.appendleft(truck)
            bridge_list.append(0)
        else:
            bridge_list.append(truck)
            sum_var += truck
        
        # print(bridge_list)
        
        
    
    # print(cnt)
        
    return cnt + bridge_length # 다 타고 다 내리기


# 0. 0 0
# 1. 0 7
# 2. 7 0
# 3. 0 4
# 4. 4 5
# 5. 5 0
# 6. 0 6
# 7. 6 0
# 8. 0 0