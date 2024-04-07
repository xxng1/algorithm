import heapq
import sys
input = sys.stdin.readline

N = int(input())

left_heap = []
right_heap = []

for i in range(N):
    x = int(input())
    # if (right_heap[0]<x):
    #     heapq.heappush(right_heap, (x))
    # else:
    #     heapq.heappush(left_heap, -(x))
    # 홀수 -> 오름차순에서 제일끝에있는거 뽑기
    # 짝수 -> 오름차순에서 제일끝에있는거 vs 내림차순에서 제일끝에있는거 에서 작은거
    # L 오름차순 R 내림차순
    if i%2 == 0: # N이 짝수일때
        heapq.heappush(left_heap, -(x))
    else:
        heapq.heappush(right_heap, (x))

    if right_heap and right_heap[0] < -left_heap[0]:
        leftValue = heapq.heappop(left_heap)
        rightValue = heapq.heappop(right_heap)

        # 값 비교 후 교체하여 왼쪽은 중간값보다 작은 값
        # 오른쪽은 중간값보다 큰 값이 들어가도록 한다.
        heapq.heappush(left_heap, -rightValue)
        heapq.heappush(right_heap, -leftValue)
	# 왼쪽부터 먼저 넣기 시작하고, (홀수이면 자동으로 가운데에 있는 원소가 나옴)
    # 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중 작은 수를 말한다.
    print(-left_heap[0])