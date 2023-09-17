import sys
sys.setrecursionlimit(10000)
m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[j][i] = 1

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c):
    global area
    arr[r][c] = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < m) or not (0 <= nc < n):
            continue
        else:
            if arr[nr][nc] == 0:
                area += 1
                dfs(nr, nc)

area = 1 # 넓이
cnt = 0 # 갯수
area_lst = []
for r in range(m):
    for c in range(n):
        if arr[r][c] == 0:
            cnt += 1
            dfs(r, c)
            area_lst.append(area)
            area = 1
print(cnt)
for area in sorted(area_lst):
    print(area, end=' ')