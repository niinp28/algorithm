# 우하좌상
from collections import deque
from pprint import pprint
dr = [0,1,0,-1]
dc = [1,0,-1,0]

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

# print(arr)
def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 0:
                    continue
                
                if arr[nr][nc] == 1:
                    arr[nr][nc] = arr[r][c] + 1
                    q.append((nr, nc))
        
    return arr[n-1][m-1]

print(bfs(0, 0))
