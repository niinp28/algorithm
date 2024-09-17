# 양치기 꿍
import sys
sys.setrecursionlimit(10**6)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def dfs(r, c):
    global K, V
    visited[r][c] = 1
    if arr[r][c] == 'k':
        K += 1
    elif arr[r][c] == 'v':
        V += 1

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if (0<=nr<N) and (0<=nc<M) and visited[nr][nc] == 0 and arr[nr][nc] != '#':
            dfs(nr, nc)
    
    


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
# v늑대 k양
ans_k, ans_v = 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != '#' and visited[i][j] == 0:
            K, V = 0, 0
            dfs(i, j)
            if K > V:
                ans_k += K
            else:
                ans_v += V
print(ans_k, ans_v)
