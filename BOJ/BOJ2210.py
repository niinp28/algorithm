# 숫자판 점프
dr = [0,1,0,-1]
dc = [1,0,-1,0]
def dfs(r, c, n):
    if len(n) == 6:
        if n not in ans:
            ans.append(n)
        return
    
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<=nr<5 and 0<=nc<5:
            dfs(nr, nc, n+arr[nr][nc])
    


arr = [list(input().split()) for _ in range(5)]

ans =  []
for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])
print(len(ans))