N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

mx = 0
def dfs(r, c, total, length):
    global mx
    if length == 4:
        mx = max(mx, total)
        return

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < N) or not (0 <= nc < M):
            continue
        else:
            if visited[nr][nc] == 0:
                if length == 2:
                    visited[nr][nc] = 1
                    dfs(r, c, total+arr[nr][nc], length+1)
                    visited[nr][nc] = 0
                visited[nr][nc] = 1
                dfs(nr, nc, total+arr[nr][nc], length+1)
                visited[nr][nc] = 0

for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs(r, c, arr[r][c], 1)
        visited[r][c] = 0

print(mx)