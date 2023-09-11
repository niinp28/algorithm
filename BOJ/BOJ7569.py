from collections import deque
from pprint import pprint
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _  in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

q = deque()
res = 0

#상 하 좌 우 위 아래
dm = [-1, 1, 0, 0, 0, 0]
dn = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

def bfs():
    while q:
        h, n, m = q.popleft()
        
        for d in range(6):
            nm = m + dm[d]
            nn = n + dn[d]
            nh = h + dh[d]

            if (0 <= nm < M and 0 <= nn < N and 0 <= nh < H and 
                arr[nh][nn][nm] == 0 and
                visited[nh][nn][nm] == 0):
                q.append((nh,nn,nm))
                arr[nh][nn][nm] = arr[h][n][m] + 1
                visited[nh][nn][nm] = 1

for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 1 and visited[h][n][m] == 0:
                q.append((h, n, m))
                visited[h][n][m] = 1

bfs()

flag = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 0:
                flag = 1
            res = max(res, arr[h][n][m])

if flag == 1:
    print(-1)
else:
    print(res - 1)