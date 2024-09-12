# 절댓값 힙

import heapq
import sys
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            a, b = heapq.heappop(heap)
            print(b)
        else:
            print(0)
        
    else:
        heapq.heappush(heap, (abs(x), x))