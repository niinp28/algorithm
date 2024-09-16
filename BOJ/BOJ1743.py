# 음식물 피하기
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
from collections import deque

def bfs(r, c):
    visited[r][c] = 1
    q = deque()
    q.append((r, c))
    cnt = 1
    while q:
        cr, cc = q.popleft()
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if (0<=nr<N) and (0<=nc<M) and arr[nr][nc] == '#' and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = 1
                cnt += 1
    return cnt


N, M, K = map(int, input().split())
arr = [['.'] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
mx = 0
for _ in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = '#'

for i in range(N):
    for j in range(M):
        if arr[i][j] == '#' and visited[i][j] == 0:
            tmp = bfs(i, j)
            if tmp >= mx:
                mx = tmp
print(mx)