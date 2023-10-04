# 점프 점프
from collections import deque
n = int(input())
lst = list(map(int, input().split()))

if n == 1:
    print(0)
else:
    visited = [0] * (n+1)
    q = deque()
    q.append(1)
    while q:
        x = q.popleft()
        if x + lst[x-1] >= n:
            print(visited[x]+1)
            break
        for i in range(1, lst[x-1]+1):
            nx = x + i
            if visited[nx] == 0:
                q.append(nx)
                visited[nx] = visited[x] + 1
    else:
        print(-1)