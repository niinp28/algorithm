# 적록색약
from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]
            if not (0 <= nx < N) or not (0 <= ny < N):
                continue
            else:
                if arr[nx][ny] == arr[x][y] and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
        
N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
green = []
cnt = 0
cnt2 = 0

for r in range(N):
    for c in range(N):
        if arr[r][c] == 'G':
            green.append((r, c))

        if visited[r][c] == 0:
            visited[r][c] == 1
            bfs(r, c)
            cnt += 1

visited = [[0] * N for _ in range(N)]
# 초록색을 빨간색으로 바꾸기
for r, c in green:
    arr[r][c] = 'R'

# 다시 실행
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            visited[r][c] == 1
            bfs(r, c)
            cnt2 += 1

print(cnt, cnt2)