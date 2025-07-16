def dfs(start, end, graph, visited):
    visited[start] = True
    
    for i in graph[start]:
        if visited[i] == False:
            if ( i != end ):
                dfs(i, end, graph, visited)
    
def solution(n, wires):
    if n == 2:
        return 0
    if n == 3:
        return 1
    
    visited = [False] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for i in range(n-1):
        a = wires[i][0]
        b = wires[i][1]
        
        graph[a].append(b)
        graph[b].append(a)
        
    ans = 1e9
    
    for a, b in wires:
        visited = [False] * (n+1)
        dfs(a, b, graph, visited)
        true_count_A = visited.count(True)
        # print(visited)
        
        # if true_count_A != 1:
        visited = [False] * (n+1)
        dfs(b, a, graph, visited)
        true_count_B = visited.count(True)

        # if true_count_B != 1:
        result = abs(true_count_A - true_count_B)

        if ans > result:
            ans = result
    
    return ans