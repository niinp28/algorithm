from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(row, col):
    q = deque()
    q.append((row, col))
    visited[row][col] = 1

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0:
                    visited[r][c] += 1
                
                if visited[nr][nc] == 0 and arr[nr][nc] != 0:
                    visited[nr][nc] = 1
                    q.append((nr, nc))

day = 0
while 1:
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if not visited[r][c] and arr[r][c] != 0:
                bfs(r, c)
                cnt += 1
    
    for r in range(N):
        for c in range(M):
            if visited[r][c] : 
                arr[r][c] -= (visited[r][c] - 1)
                if arr[r][c] < 0:
                    arr[r][c] = 0
    
    day += 1
    if cnt == 0:
        print(0)
        exit(0)
    if cnt >= 2:
        break
print(day-1)