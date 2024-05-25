# 탈출
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def bfs(rc, t):
    q = deque()
    for r, c in rc:
        q.append((r, c))
        if t == 1:
            visited[r][c] = 1
        else:
            watered[r][c] = 1
    while q:
        a, b = q.popleft()
        for d in range(4):
            nr = a + dr[d]
            nc = b + dc[d]
            if (0<=nr<N) and (0<=nc<M):
                if t == 1:  # 고슴도치 bfs
                    if (arr[nr][nc] == '.' or arr[nr][nc] == 'D') and visited[nr][nc] == 0:
                        if watered[nr][nc] > visited[a][b] + 1 or watered[nr][nc] == 0:
                            visited[nr][nc] = visited[a][b] + 1
                            q.append((nr, nc))
                else:  # 물 bfs
                    if (arr[nr][nc] == '.' or arr[nr][nc] == 'S') and watered[nr][nc] == 0:
                        watered[nr][nc] = watered[a][b] + 1
                        q.append((nr, nc))
    
    
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
watered = [[0]*M for _ in range(N)]
water_position = []
start = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S':
            start.append((i, j))
        elif arr[i][j] == 'D':
            gr, gc = i, j
        elif arr[i][j] == '*':
            water_position.append((i, j))

bfs(water_position, 2)
# print(watered)
bfs(start, 1)
# print(visited)

if visited[gr][gc] == 0:
    print('KAKTUS')
else:
    print(visited[gr][gc]-1)