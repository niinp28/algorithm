# 최대힙

import heapq
import sys
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            a = heapq.heappop(heap)
            print(abs(a))
        else:
            print(0)
        
    else:
        heapq.heappush(heap, -x)