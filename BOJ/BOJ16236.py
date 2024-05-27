# 아기상어
# from pprint import pprint
from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def bfs(r, c):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    while q:
        a, b = q.popleft()
        for d in range(4):
            nr = a + dr[d]
            nc = b + dc[d]
            if (0<=nr<N) and (0<=nc<N) and visited[nr][nc] == 0 and arr[nr][nc] <= state:
                visited[nr][nc] = visited[a][b] + 1
                q.append((nr, nc))
    return visited       
              
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
fishes = [[] for _ in range(7)]
possible = []
sr, sc = 0, 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            sr = i
            sc = j
            arr[i][j] = 0
        elif arr[i][j] != 0:
            fishes[arr[i][j]].append((i, j))
state = 2
eat = 0
time = 0
possible += fishes[1]
# print(possible)
while possible:
    tmp = []
    res = bfs(sr, sc)
    # pprint(res)
    for a, b in possible:
        if res[a][b] != 0:
            tmp.append((a, b, res[a][b]))
    if not tmp:
        break
    tmp.sort(key=lambda x: (-x[2], -x[0], -x[1]))
    # print(f'임시 : {tmp}')
    c, d, e = tmp.pop()
    possible.remove((c, d))

    arr[c][d] = 0
    eat += 1

    time += res[c][d]-1
    sr, sc = c, d
    # print(time)
    if state == eat:
        state += 1
        eat = 0
        if state < 8:
            possible += fishes[state-1]
print(time)
# print(time)

