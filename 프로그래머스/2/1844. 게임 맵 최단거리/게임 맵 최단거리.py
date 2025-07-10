from collections import deque

def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(maps[0]) # 가로
    m = len(maps) # 세로
    
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    queue.append((nx, ny))
        
    
#     for i in maps:
#         print(i)
    
    
    if maps[-1][-1] == 1:
        answer = -1
    else:
        answer = maps[-1][-1]
    
    
    
    
    
    return answer