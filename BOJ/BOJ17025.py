# Icy Perimeter
from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def bfs(r, c):
    global a, p
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    a += 1
    while q:
        e, f = q.popleft()        
        for d in range(4):
            nr = e + dr[d]
            nc = f + dc[d]
            if (0<=nr<N) and (0<=nc<N) and arr[nr][nc] == '#':
                if visited[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    a += 1
            else:
                p += 1


N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '#' and visited[i][j] == 0:
            a, p = 0, 0
            bfs(i, j)
            ans.append((a, p))
ans.sort(key=lambda x: (x[0], -x[1]))
res = ans[-1]
print(res[0], res[1])