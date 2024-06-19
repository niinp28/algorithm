# 경쟁적 전염
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
from collections import deque

def bfs(second, X, Y):
    q = deque(initial)
    t = 0
    while q:
        if t == second:
            break
        for _ in range(len(q)):
            a, b, n = q.popleft()
            for d in range(4):
                nr = a + dr[d]
                nc = b + dc[d]
                if (0<=nr<N) and (0<=nc<N):
                    if arr[nr][nc] == 0:
                        arr[nr][nc] = arr[a][b]
                        q.append((nr, nc, n))
        t += 1
    return arr[X-1][Y-1]

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
s, x, y = map(int, input().split())
initial = []

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            initial.append((i, j, arr[i][j]))

initial.sort(key=lambda x: x[2])
ans = bfs(s, x, y)
# print(arr)
print(ans)