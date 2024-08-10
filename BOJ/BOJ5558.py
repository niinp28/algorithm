from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def bfs(r, c):
    global lv, ans
    q = deque()
    q.append((r, c))
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    flag = False
    while q:
        x, y = q.popleft()
        if arr[x][y] != '.' and arr[x][y] != 'S':
            if int(arr[x][y]) <= lv:
                arr[x][y] = 'S'
                lv += 1
                flag = True
                V, X, Y =  visited[x][y] - 1, x, y
                break
        for d in range(4):
            nr = x + dr[d]
            nc = y + dc[d]
            if (0<=nr<N) and (0<=nc<M) and visited[nr][nc] == 0:
                if arr[nr][nc] != 'X':
                    visited[nr][nc] = visited[x][y] + 1
                    q.append((nr, nc))
    if flag:
        return (V, X, Y)
    else:
        return (-1, -1, -1)


N, M, C = map(int, input().split())
arr = [list(input()) for _ in range(N)]
lv = 1
ans = 0
sr, sc = 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S':
            sr, sc = i, j

while 1:
    dist, res_x, res_y = bfs(sr, sc)
    if dist == -1 and res_x == -1 and res_y == -1:
        break
    ans += dist
    sr, sc = res_x, res_y
print(ans)
