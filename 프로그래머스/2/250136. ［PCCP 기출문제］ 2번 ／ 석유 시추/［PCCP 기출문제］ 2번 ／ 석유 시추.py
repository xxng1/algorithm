from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    # 각 석유 덩어리에 고유 ID를 부여하고 크기를 저장
    oil_groups = {}  # {group_id: size}
    group_map = [[-1] * m for _ in range(n)]  # 각 위치의 그룹 ID
    group_id = 0
    
    # 모든 석유 덩어리를 찾고 크기를 계산
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and group_map[i][j] == -1:
                # 새로운 석유 덩어리 발견
                size = bfs_group(i, j, land, group_map, group_id)
                oil_groups[group_id] = size
                group_id += 1
    
    max_oil = 0
    
    # 각 열에 대해 석유량 계산
    for col in range(m):
        visited_groups = set()
        total_oil = 0
        
        for row in range(n):
            if land[row][col] == 1:
                gid = group_map[row][col]
                if gid not in visited_groups:
                    visited_groups.add(gid)
                    total_oil += oil_groups[gid]
        
        max_oil = max(max_oil, total_oil)
    
    return max_oil

def bfs_group(start_y, start_x, land, group_map, group_id):
    """특정 석유 덩어리의 크기를 계산하고 그룹 ID를 할당"""
    queue = deque([(start_y, start_x)])
    group_map[start_y][start_x] = group_id
    
    n = len(land)
    m = len(land[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    size = 1
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if (0 <= ny < n and 0 <= nx < m and 
                land[ny][nx] == 1 and group_map[ny][nx] == -1):
                
                group_map[ny][nx] = group_id
                queue.append((ny, nx))
                size += 1
    
    return size