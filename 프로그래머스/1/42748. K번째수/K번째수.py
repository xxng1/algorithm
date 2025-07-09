def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        a = commands[i][0]
        b = commands[i][1]
        
        print(a-1, b-1)
        temp_arr = sorted(array[a-1:b])
        
        answer.append(temp_arr[commands[i][2]-1])
    
    return answer