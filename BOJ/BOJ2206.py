# 벽 부수고 이동하기
from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs():
    q = deque()
    q.append((0, 0, 1, 0))
    visited[0][0][0] = 1
    while q:
        a, b, cnt, wall = q.popleft()
        if a == N-1 and b == M-1:
            return cnt
        for d in range(4):
            nr = a + dr[d]
            nc = b + dc[d]
            if (0<=nr<N) and (0<=nc<M):
                # 벽 X, 방문 X => 이동
                if arr[nr][nc] == 0 and not visited[nr][nc][wall]:
                    visited[nr][nc][wall] = 1
                    q.append((nr, nc, cnt+1, wall))
                # 벽 O, 벽 안부쉈을 때는 벽 부수고 이동
                elif arr[nr][nc] == 1 and wall == 0:
                    visited[nr][nc][1] = 1
                    q.append((nr, nc, cnt+1, 1))
    return -1

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

print(bfs())

