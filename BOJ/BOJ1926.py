# 그림
from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def bfs(r, c, cnt):
    global mx
    q = deque()
    q.append((r, c))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]
            if not (0 <= nx < n) or not (0 <= ny < m):
                continue
            else:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
    if mx <= cnt:
        mx = cnt
    

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
number = 0
mx = 0

for r in range(n):
    for c in range(m):
        if arr[r][c] != 0 and visited[r][c] == 0:
            visited[r][c] = 1
            bfs(r, c, 1)
            number += 1

print(number)
print(mx)
