# 벽 부수고 이동하기 3
# 벽 부수고 이동하기 2

from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs():
    q = deque()
    q.append((0, 0, 1, K, 1))
    visited[0][0][0] = 1
    is_day = 0
    while q:
        a, b, cnt, wall, is_day = q.popleft()
        if a == N-1 and b == M-1:
            return cnt
        for d in range(4):
            nr = a + dr[d]
            nc = b + dc[d]
            if (0<=nr<N) and (0<=nc<M):
                if wall == 0:
                    if arr[nr][nc] == 0 and not visited[nr][nc][0]:
                        q.append((nr, nc, cnt+1, 0, (is_day+1)%2))
                        visited[nr][nc][0] = 1
                else:
                    if arr[nr][nc] == 0 and not visited[nr][nc][wall]:
                        q.append((nr, nc, cnt+1, wall, (is_day+1)%2))
                        visited[nr][nc][wall] = 1
                    elif arr[nr][nc] == 1 and not visited[nr][nc][wall-1]:
                        if is_day:
                            q.append((nr, nc, cnt+1, wall-1, (is_day+1)%2))
                            visited[nr][nc][wall-1] = 1
                        else:
                            q.append((a, b, cnt+1, wall, (is_day+1)%2))

    return -1

N, M, K = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
for i in range(K):
    visited[0][0][i] = 1
print(bfs())

