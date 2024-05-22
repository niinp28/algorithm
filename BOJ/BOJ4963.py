# 섬의 개수
dr = [0,1,0,-1, 1, 1, -1, -1]
dc = [1,0,-1,0, 1, -1, 1, -1]
from collections import deque
def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    while q:
        a, b = q.popleft()
        for d in range(8):
            nr = a + dr[d]
            nc = b + dc[d]
            if (0<=nr<h) and (0<=nc<w) and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr, nc))

    
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = []
    for _ in range(h):
        a = list(map(int, input().split()))
        arr.append(a)
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1
    print(cnt)
