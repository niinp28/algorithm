# N번째 큰수
from heapq import heappush, heappop
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

mx_heap = []
for c in range(N):
    heappush(mx_heap, (-arr[N-1][c], c, N-1))

for _ in range(N):  # N번째 큰수를 찾아야하니 N만큼 시행
    number, col, row = heappop(mx_heap)

    if row > 0:
        heappush(mx_heap, (-arr[row-1][col], col, row-1))
print(-number)