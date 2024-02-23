# 상범 빌딩
from collections import deque
dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]
def bfs(r, c):
    q = deque()
    q.append((r, c))
    while q:
        a, b = q.popleft()
        if a == gr and b == gc:
            print(visited[a][b]-1)
            return
        for d in range(8):
            nr = a + dr[d]
            nc = b + dc[d]
            if (0<=nr<N) and (0<=nc<N) and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = visited[a][b] + 1
                
                    
    


T = int(input())
for _ in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    sr, sc = map(int, input().split())
    gr, gc = map(int, input().split())
    visited[sr][sc] = 1
    bfs(sr, sc)
    