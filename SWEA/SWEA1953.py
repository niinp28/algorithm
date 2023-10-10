# 탈주범 검거
from collections import deque
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
pipes = [[], [0,1,2,3], [1,3], [0,2], [0,3], [0,1], [1,2], [2,3]]
def bfs(r, c):
    q = deque()
    q.append((r, c))
    while q:
        x, y = q.popleft()
        directions = pipes[arr[x][y]]
        for d in directions:
            nx = x + dr[d]
            ny = y + dc[d]
            if (0<=nx<n) and (0<=ny<m) and visited[nx][ny] == 0 and arr[nx][ny] != 0:
                new_pipe = pipes[arr[nx][ny]]
                for d in new_pipe:
                    nnx = nx + dr[d]
                    nny = ny + dc[d]
                    if nnx == x and nny == y:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
        

T = int(input())
for tc in range(1, 1+T):
    n, m, r, c, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    cnt = 0
    bfs(r, c)
    
    for i in range(n):
        for j in range(m):
            if 1 <= visited[i][j] <= L:
                cnt += 1
    print(f'#{tc} {cnt}')