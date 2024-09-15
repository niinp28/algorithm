# 전투
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
from collections import deque
def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    current = arr[r][c]
    cnt = 1
    while q:
        a, b = q.popleft()
        for d in range(4):
            nr = a + dr[d]
            nc = b + dc[d]
            if (0<=nr<N) and (0<=nc<M) and visited[nr][nc] == 0:
                if arr[nr][nc] == current:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    cnt += 1
    return cnt ** 2            

M, N = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
w, b = 0, 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            if arr[i][j] == 'W':
                w += bfs(i, j)
            else:
                b += bfs(i, j)
print(w, b)