# 토마토
from collections import deque
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
q = deque()
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def bfs():
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0<=nr<n) or not (0 <= nc <m):
                continue
            else:
                if arr[nr][nc] == -1:
                    continue
                elif arr[nr][nc] == 0 and not visited[nr][nc]:
                    arr[nr][nc] = arr[r][c] + 1
                    visited[nr][nc] = 1
                    q.append((nr, nc))


for r in range(n):
    for c in range(m):
        if arr[r][c] == 1 and visited[r][c] == 0:
            q.append((r, c))
            visited[r][c] = 1
bfs()
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            exit(0)
        ans = max(ans, arr[i][j])
print(ans-1)