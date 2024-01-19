# 불
from collections import deque
from pprint import pprint
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
            if (0<=nr<h) and (0<=nc<w) and arr[nr][nc] != '#' and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[a][b] + 1
    
    

for _ in range(int(input())):
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    burned = [[0] * w for _ in range(h)]
    path = [[0] * w for _ in range(h)]
    fire_start = []
    runner_start = []

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                runner_start.append((i, j))
            elif arr[i][j] == '*':
                fire_start.append((i, j))

    bfs(runner_start, path)
    bfs(fire_start, burned)
    ans = 10000000
    flag = False
    for i in range(h):
        for j in range(w):
            if i == 0 or i == h-1 or j == 0 or j == w-1:
                if not path[i][j]:
                    continue
                else:
                    if path[i][j] < burned[i][j] or path[i][j] and not burned[i][j]:
                        flag = True
                        ans = min(ans, path[i][j])
    
    if flag:
        print(ans)
    else:
        print('IMPOSSIBLE')
'''
5
4 3
####
#*@.
####
7 6
###.###
#*#.#*#
#.....#
#.....#
#..@..#
#######
7 4
###.###
#....*#
#@....#
.######
5 5
.....
.***.
.*@*.
.***.
.....
3 3
###
#@#
###
'''