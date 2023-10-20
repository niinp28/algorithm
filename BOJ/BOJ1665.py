# 힙 사용, 우선순위 큐
import heapq
import sys

N = int(sys.stdin.readline())
min_heap = []
max_heap = []
heapq.heapify(min_heap)
heapq.heapify(max_heap)
ans = []
for i in range(N):
    number = int(sys.stdin.readline())
    if i % 2:  # 오른쪽 힙(최소힙) 
        heapq.heappush(min_heap, number)
    else:  # 왼쪽 힙(최대 힙)
        heapq.heappush(max_heap, (-number, number))

    #  첫 번째에는 그냥 첫 번째 요소를 부르면 됨
    if not i:
        ans.append(number)
    else:
        #  왼쪽 힙의 최대가 오른쪽 힙의 최소보다 크면 안된다
        if max_heap[0][1] > min_heap[0]:
            left = heapq.heappop(max_heap)
            right = heapq.heappop(min_heap)
            heapq.heappush(min_heap, left[1])
            heapq.heappush(max_heap, (-right, right))
        
        ans.append(max_heap[0][1])

for num in ans:
    print(num)