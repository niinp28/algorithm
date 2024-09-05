# 순회강연
import heapq

N = int(input())
lec = []
for _ in range(N):
    p, d = map(int, input().split())
    lec.append((d, p))

lec.sort()
q = []

for le in lec:
    d, p = le
    heapq.heappush(q, p)
    if len(q) > d:
        heapq.heappop(q)

print(sum(q))

