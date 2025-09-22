import sys
sys.setrecursionlimit(10**6)

def solution(n, lighthouse):
    if n <= 3:
        return 1
    
    answer = 0
    
    visited = [False] * (n+1)
    graph = [[] for _ in range(n+1)]
    dp = [[0, 0] for _ in range(n+1)]
    
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
    
    
    def dfs(start):
        visited[start] = True
        dp[start][0] = 0
        dp[start][1] = 1
        
        
        for i in graph[start]:
            if not visited[i]:
                dfs(i)
                dp[start][0] += dp[i][1]
                dp[start][1] += min(dp[i][0], dp[i][1])
    
    
    dfs(1)
    
    # print(dp)
    
    return min(dp[1][0], dp[1][1])