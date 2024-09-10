from collections import deque
from pprint import pprint
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def move(r, c, area, name):
    q = deque()
    q.append((r, c, area))
    visited[r][c] = 1
    while q:
        a, b, c = q.popleft()
        if c <= 0:
            break
        for d in range(4):
            nr = a + dr[d]
            nc = b + dc[d]
            if (0<=nr<N) and (0<=nc<M) and arr[nr][nc] == '.' and visited[nr][nc] == 0:
                q.append((nr, nc, c-1))
                arr[nr][nc] = name
                visited[nr][nc] = visited[a][b] + 1
               
    

N, M, P = map(int, input().split())
players = list(map(int, input().split()))
player = {}
for i in range(len(players)):
    player[i+1] = players[i]

arr = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
while True:
    start = []
    cnt = 0
    flag = False
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '.':
                flag = True
            if arr[i][j] != '.':
                if arr[i][j] != '#':
                    start.append((i, j, player[int(arr[i][j])], arr[i][j]))

    if flag:        
        for i, j, k, l in start:
            move(i, j, k, l)
    else:
        break

res = [0] * P
for i in range(N):
    for j in range(M):
        if arr[i][j] != '#':
            res[int(arr[i][j])-1] += 1
print(' '.join(map(str, res)))
