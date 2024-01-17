# 카드 정렬하기
from heapq import heapify, heappush, heappop
N = int(input())  # 10만
ans = 0
lst = []
heapify(lst)
for _ in range(N):
    heappush(lst , int(input()))

while True:
    if N == 1:
        break
    a = heappop(lst)
    b = heappop(lst)
    c = a+b
    ans += c
    if lst:
        heappush(lst, c)
    else:
        break

print(ans)