cnt = 0


def dfs(start, visited, n, computers):
    global cnt
    visited[start] = True

    for i in range(n):
        if computers[start][i] == 1:
            if visited[i] == False:
                cnt += 1
                dfs(i, visited, n, computers)

def solution(n, computers):
    visited = [False] * n
    
    for i in range(n):
        dfs(i, visited, n, computers)
        
    
    
    return (n - cnt )