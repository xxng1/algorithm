C = int(input())


def backtracking(visited, depth, total):
    global answer
    if depth == 11:
        answer = max(answer, total)
        return 
    
    for i in range(11):
        if visited[i] == False and arr[i][depth] != 0:
            visited[i] = True
            backtracking(visited, depth + 1, total + arr[i][depth])
            visited[i] = False


for _ in range(C):
    arr = []
    
    for i in range(11):
        arr.append(list(map(int, input().split())))

    visited = [False] * 11
    answer = 0



    backtracking(visited, 0, 0)
    print(answer)