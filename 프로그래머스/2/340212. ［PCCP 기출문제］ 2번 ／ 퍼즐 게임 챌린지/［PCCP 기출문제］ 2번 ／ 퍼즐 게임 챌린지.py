def simulation(diffs, level, times):
    result = 0
    
    for i in range(len(diffs)):
        if level >= diffs[i]:
            result += times[i]
        else:
            tmp = (times[i-1] + times[i]) * (diffs[i] - level) + times[i]
            result += tmp
    
    return result

def solution(diffs, times, limit):
    answer = 0
    level = 0
    
    # print(simulation(diffs, level, times))
    
    left = 1
    right = 1000000000000001
    
    while left <= right:
        mid = ( left + right ) // 2
        
        
        tmp = simulation(diffs, mid, times)
        
        # if tmp < limit:
        if limit < tmp:
            left = mid + 1
        else:
            right = mid - 1
        
    # print(left, right)
    return left