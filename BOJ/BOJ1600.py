# 말이 되고픈 원숭이
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

dr2 = [1, 2, 2, 1, -1, -2, -2, -1]
dc2 = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(n):
    q = deque()
    q.append((0, 0, n))
    visited = [[[0] * (n+1) for _ in range(M)] for _ in range(N)]
    while q:
        x, y, k = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][k]
        
        if k > 0:
            for d in range(8):
                nr = x + dr2[d]
                nc = y + dc2[d]
                if (0<=nr<N) and (0<=nc<M) and arr[nr][nc] != 1 and visited[nr][nc][k-1] == 0:
                    visited[nr][nc][k-1] = visited[x][y][k] + 1
                    q.append((nr, nc, k-1))

        for d in range(4):
            nr = x + dr[d]
            nc = y + dc[d]
            if (0<=nr<N) and (0<=nc<M) and arr[nr][nc] != 1 and visited[nr][nc][k] == 0:
                visited[nr][nc][k] = visited[x][y][k] + 1
                q.append((nr, nc, k))

    return -1


K = int(input())
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = bfs(K)
print(ans)