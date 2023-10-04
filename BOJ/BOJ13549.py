# 숨바꼭질 3
from collections import deque
def bfs(n, k):
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        x = q.popleft()
        if x == k:
            return
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= 100000 and visited[nx] == -1:
                if nx == x * 2:
                    visited[nx] = visited[x] # 이전 과정과 같은 초(0초)
                    q.appendleft(nx)
                else:
                    visited[nx] = visited[x] + 1
                    q.append(nx)
    

n, k = map(int, input().split())
visited = [-1] * (100001)

bfs(n, k)
print(visited[k])

