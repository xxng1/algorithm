import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    
    for i in scoville:
        heapq.heappush(heap, i)
    
    while True:
        if heap[0] >= K: # min(scoville)
            break
        if len(heap) < 2:
            break
        
        A = heapq.heappop(heap)
        B = heapq.heappop(heap)
        
        heapq.heappush(heap, A + ( B * 2 ))
        answer += 1
        
    # print(heap)
    
    if heap[0] < K:
        return -1
    return answer