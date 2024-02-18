# 컴백홈
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def dfs(r, c):
    global cnt
    if visited[r][c] > k:
        return
    
    if r == 0 and c == m-1:
        if visited[r][c] == k:
            cnt += 1
    else:
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0<=nr<n) and (0<=nc<m) and arr[nr][nc] != 'T' and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                dfs(nr,nc)
                visited[nr][nc] = 0
    
        


n, m, k = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0
visited[n-1][0] = 1
dfs(n-1, 0)

print(cnt)
'''
3 4 6
....
.T..
....
'''