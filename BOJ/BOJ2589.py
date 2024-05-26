# 보물섬
from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def bfs(r, c, v):
    global mx
    q = deque()
    q.append((r, c))
    tmp = 0
    v[r][c] = 1
    while q:
        a, b = q.popleft()
        for d in range(4):
            nr = a + dr[d]
            nc = b + dc[d]
            if (0<=nr<N) and (0<=nc<M) and v[nr][nc] == 0 and arr[nr][nc] == 'L':
                q.append((nr, nc))
                v[nr][nc] = v[a][b] + 1
                tmp = max(tmp, v[nr][nc])
    return tmp-1
    

    

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
res = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            res = max(res, bfs(i, j, visited))
print(res)