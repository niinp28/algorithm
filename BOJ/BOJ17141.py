# 연구소 2
from pprint import pprint
from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(virus_starts, visited):
    q = deque()
    for r, c in virus_starts:
        q.append((r, c))
        visited[r][c] = 1
    while q:
        a, b = q.popleft()
        for d in range(4):
            nr = a + dr[d]
            nc = b + dc[d]
            if (0<=nr<N) and (0<=nc<N) and arr[nr][nc] != 1:
                if not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[a][b] + 1
    for row in visited:
        if 0 in row:
            return -1
                
def comb(level, start):
    global ans
    if level == M:
        visited = [[0] * N for _ in range(N)]
        for wi, wj in walls:
            visited[wi][wj] = -1
        print(bfs(rs, visited))
        pprint(visited)
        ans = min(bfs(rs, visited), ans)
    else:
        for i in range(start, len(virus_start)):
            rs[level] = virus_start[i]
            comb(level+1, i+1)
    

                
    


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus_start = []
walls = []
rs = [0] * M
ans = 1000
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus_start.append((i, j))
        elif arr[i][j] == 1:
            walls.append((i, j))
comb(0, 0)
# print(ans)
