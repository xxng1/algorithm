def solution(plans):
    answer = []
    stack = []

    for i in range(len(plans)):
        a, b = map(int, plans[i][1].split(':'))
        plans[i][1] = a * 60 + b
        plans[i][2] = int(plans[i][2])

    plans.sort(key = lambda x : x[1])
    
    print(plans)
    # [name, start, playtime]

    for i in range(len(plans) - 1):
        stack.append(plans[i])
        gap = plans[i+1][1] - plans[i][1]

        # print(gap)
        while stack and gap:
            if stack[-1][2] <= gap:
                a, b, c = stack.pop()
                gap -= c
                answer.append(a)
                # print("Asd")
            else:
                stack[-1][2] -= gap
                gap = 0

    answer.append(plans[-1][0])

    for i in range(len(stack)):
        answer.append(stack[~i][0])
            
    return answer