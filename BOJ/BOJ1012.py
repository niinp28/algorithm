dr = [0, 1, 0 ,-1]
dc = [1, 0, -1, 0]
from collections import deque
def bfs(r, c):
    q = deque()
    q.append((r, c))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]
            if not (0 <= nx < N) or not (0 <= ny < M):
                continue
            else:
                if visited[nx][ny] == 0 and arr[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    ans = 0

    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1 and visited[r][c] == 0:
                visited[r][c] = 1
                bfs(r, c)
                ans += 1
    print(ans)