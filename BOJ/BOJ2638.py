# 치즈
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
from collections import deque

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    while q:
        x, y = q.popleft()   
        for d in range(4):
            nr = x + dr[d]
            nc = y + dc[d]
            if (0<=nr<N) and  (0<=nc<M):
                # 공기일땐 큐 추가
                if visited[nr][nc] == 0 and arr[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                # 치즈일땐 접촉면의 갯수 업데이트
                elif arr[nr][nc] == 1:
                    visited[nr][nc] += 1

    

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
t = 0
while True:
    visited = [[0] * M for _ in range(N)]
    bfs(0, 0)
    air = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                air += 1
            if visited[i][j] > 1:
                arr[i][j] = 0
    
    if air == N*M:
        break
    t += 1
print(t)
    
    
