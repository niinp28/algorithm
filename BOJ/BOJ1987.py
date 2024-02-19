# 알파벳
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r, c, length):
    global mx
    mx = max(mx, length)
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if (0<=nr<N) and (0<=nc<M) and visited[nr][nc] == 0 and arr[nr][nc] not in apb:
                # visited[nr][nc] = 1
                apb.add(arr[nr][nc])
                dfs(nr, nc, length+1)
                # visited[nr][nc] = 0
                apb.remove(arr[nr][nc])
    



N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
apb = set()
visited[0][0] = 1
apb.add(arr[0][0])
mx = 1
dfs(0, 0, mx)
print(mx)
'''
2 4
CAAB
ADCB

3 6
HFDFFB
AJHGDH
DGAGEH

5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
'''