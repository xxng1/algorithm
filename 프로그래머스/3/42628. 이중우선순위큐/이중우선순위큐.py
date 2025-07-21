# import heapq

# def solution(operations):
#     answer = []
    
#     heap_A = [] # 최대힙
#     heap_B = [] # 최소힙
    
#     for command in operations:
#         if command[0] == 'I':
#             x = int(command[2:])
            
#             heapq.heappush(heap_A, (-x, x))
#             heapq.heappush(heap_B, (x))
        
#         elif command[0] == 'D':
#             if command[2] == '-':
#                 if heap_B:
#                     heapq.heappop(heap_B)
#             else:
#                 if heap_A:
#                     heapq.heappop(heap_A)
    
#     if heap_A:
#         maximum = heapq.heappop(heap_A)[1]
    
#     if heap_B:
#         minimum = heapq.heappop(heap_B)
    
    
#     return [maximum, minimum]



import heapq

def solution(operations):
    
    arr = []
    
    for command in operations:
        if command[0] == 'I':
            x = int(command[2:])
            
            heapq.heappush(arr, x)
        
        elif command[0] == 'D':
            if command[2] == '-':
                if arr:
                    heapq.heappop(arr)
            else:
                if arr:
                    arr.pop(arr.index(max(arr)))
        

    
    if not arr:
        return [0, 0]
    else:
        return [max(arr), min(arr)]