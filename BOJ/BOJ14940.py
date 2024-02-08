# 쉬운 최단 거리
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
from collections import deque
def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 0
    while q:
        a, b = q.popleft()
        for d in range(4):
            nr = a + dr[d]
            nc = b + dc[d]
            if (0<=nr<N) and (0<=nc<M) and not visited[nr][nc]:
                if arr[nr][nc] == 0:
                    continue
                else:
                    visited[nr][nc] = visited[a][b] + 1
                    q.append((nr, nc))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
sr, sc = 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            bfs(i, j)
            sr = i
            sc = j
visited[sr][sc] = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if arr[i][j] == 1:
                visited[i][j] = -1
for row in visited:
    print(*row)

'''
15 15
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
'''