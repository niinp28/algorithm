# 불!
from pprint import pprint
from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def bfs(start, visited):
    q = deque()
    for r, c in start:
        q.append((r, c))
        visited[r][c] = 1
    while q:
        a, b = q.popleft()
        for d in range(4):
            nr = a + dr[d]
            nc = b + dc[d]
            if (0<=nr<R) and (0<=nc<C) and not visited[nr][nc] and arr[nr][nc] != '#':
                q.append((nr, nc))
                visited[nr][nc] = visited[a][b] + 1


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
jihun_start = []
fire_start = []
visited = [[0] * C for _ in range(R)]
burned = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'J':
            jihun_start.append((i, j))
        elif arr[i][j] == 'F':
            fire_start.append((i, j))

bfs(jihun_start, visited)
bfs(fire_start, burned)
ans = 10000
for i in range(R):
    for j in range(C):
        if i == 0 or i == R-1 or j == 0 or j == C-1:
            if not visited[i][j]:
                continue
            else:
                if visited[i][j] < burned[i][j] or visited[i][j] and not burned[i][j]:
                    ans = min(ans, visited[i][j])


if ans == 10000:
    print('IMPOSSIBLE')
else:
    print(ans)

'''
4 4
####
#JF#
#..#
#..#
'''