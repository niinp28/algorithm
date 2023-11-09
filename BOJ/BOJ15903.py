# 카드 합체 놀이
from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
number = list(map(int, input().split()))

heapify(number)

while m:
    a = heappop(number)
    b = heappop(number)

    x = a+b
    a = x
    b = x
    heappush(number, a)
    heappush(number, b)
    m -= 1

print(sum(number))