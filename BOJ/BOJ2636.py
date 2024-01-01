# 치즈
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        a, b = q.popleft()
        for d in range(4):
            na = a + dr[d]
            nb = b + dc[d]
            if (0<=na<N) and (0<=nb<M) and visited[na][nb] == 0:
                if arr[na][nb] == 0:
                    q.append((na, nb))
                    visited[na][nb] = 1
                elif arr[na][nb] == 1:
                    remove.add((na, nb))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


time = 0
recent = 0
while True:
    visited = [[0] * M for _ in range(N)]
    remove = set()
    bfs(0, 0)
    if len(remove):
        recent = len(remove)
        for i, j in list(remove):
            arr[i][j] = 0
        time += 1
    else:
        break
print(time)
print(recent)
