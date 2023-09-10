# 재귀 깊이 지정
import sys
sys.setrecursionlimit(100000)

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def dfs(r, c, k):
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] > k:
            visited[nr][nc] = 1
            dfs(nr, nc, k)
    

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

res = 1

for h in range(max(map(max, arr))):    
    visited = [[0] * N for _ in range(N)]
    safe_area = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and visited[i][j] == 0:
                safe_area += 1
                visited[i][j] = 1
                dfs(i, j, h)
    
    res = max(res, safe_area)
print(res)