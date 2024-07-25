# 양
from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def bfs(r, c):
    sheep = 0
    wolf = 0
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    while q:
        a, b = q.popleft()
        if arr[a][b] == 'o':
            sheep += 1
        elif arr[a][b] == 'v':
            wolf += 1
        for d in range(4):
            nr = a + dr[d]
            nc = b + dc[d]
            if (0<=nr<N) and (0<=nc<M) and visited[nr][nc] == 0 and arr[nr][nc] != '#':
                q.append((nr, nc))
                visited[nr][nc] = 1
    return sheep, wolf


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
total_sheep = 0
total_wolf = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and (arr[i][j] == 'o' or arr[i][j] == 'v'):
            sheep, wolf = bfs(i, j)            
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf
print(total_sheep, total_wolf)

