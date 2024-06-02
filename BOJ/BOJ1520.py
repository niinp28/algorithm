# 내리막길
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def dfs(r, c):
    global ans
    if not (0<=r<N) and (0<=c<M):
        return 0
    if dp[r][c] != -1:
        return dp[r][c]
    if r == N-1 and c == M-1:
        return 1
    
    tmp = 0
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if (0<=nr<N) and (0<=nc<M) and arr[nr][nc] < arr[r][c]:
            
            tmp += dfs(nr, nc)

    dp[r][c] = tmp      
    return dp[r][c]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*M for _ in range(N)]
ans = 0

dfs(0, 0)
print(dp[0][0])