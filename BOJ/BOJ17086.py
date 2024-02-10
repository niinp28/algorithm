# 아기 상어 2
dr = [0, 1, 0, -1, 1, 1, -1, -1]
dc = [1, 0, -1, 0, 1, -1, 1, -1]
from collections import deque

def bfs(start):
    q = deque()
    for r, c, in start:
        q.append((r, c))
        visited[r][c] = 1
    
    while q:
        a, b = q.popleft()
        for d in range(8):
            nr = a + dr[d]
            nc = b + dc[d]
            if (0<=nr<N) and (0<=nc<M) and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = visited[a][b] + 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
sharks = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            sharks.append((i, j))

bfs(sharks)
mx = 0
for row in visited:
    tmp = max(row)
    if mx < tmp:
        mx = tmp
print(mx-1)