def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    # print(participant)
    # print(completion)
    
    visited = False
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            visited = True
            break
    
    if visited:
        answer = participant[i]
    else:
        answer = participant[-1]
    
    
    return answer