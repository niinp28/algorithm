# 인구 이동
from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(row, col):
    global flag
    union = []
    cnt = arr[row][col]
    q = deque()
    q.append((row, col))
    union.append((row, col))
    visited[row][col] = 1
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0<=nr<N) and (0<=nc<N) and not visited[nr][nc]:
                if L <= abs(arr[nr][nc]-arr[r][c]) <= R:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    union.append((nr, nc))
                    cnt += arr[nr][nc]

    population = int(cnt / len(union))
    if len(union) > 1:
        flag = True
    for a, b in union:
        arr[a][b] = population

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
day = 0

while True:
    visited = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)
    if flag == True:
        day += 1
    else:
        break
print(day)