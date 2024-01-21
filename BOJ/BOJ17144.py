# 미세먼지 안녕!
# from pprint import pprint
from collections import deque
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
# 확산 -> bfs
def spread(dusts):
    for r, c, v in dusts:
        dust_spread = int(v / 5)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < M) and arr[nr][nc] != -1:
                arr[nr][nc] += dust_spread
                arr[r][c] -= dust_spread
    

def make_blow_area(r, c, direc, lst, q):
    br, bc = r, c
    if direc == 'upper':
        for d in range(4, 0, -1):
            while True:
                r = r + dr[d%4]
                c = c + dc[d%4]
                if r == br and c == bc:
                    return
                else:
                    if (0<=r<N) and (0<=c<M):
                        lst.append((r, c))
                        q.append(arr[r][c])
                    else:
                        r = r - dr[d%4]
                        c = c - dc[d%4]
                        break
                

    elif direc == 'lower':
        for d in range(4):
            while True:
                r = r + dr[d%4]
                c = c + dc[d%4]
                if r == br and c == bc:
                    return
                else:
                    if (0<=r<N) and (0<=c<M):
                        lst.append((r, c))
                        q.append(arr[r][c])                        
                    else:
                        r = r - dr[d%4]
                        c = c - dc[d%4]
                        break

# 공기청정기 작동
def blow(ud, ld):
    global arr, upper_area, lower_area
    ud.pop()
    ud.appendleft(0)
    ld.pop()
    ld.appendleft(0)
    for i in range(len(ud)):
        arr[upper_area[i][0]][upper_area[i][1]] = ud[i]
    for i in range(len(ld)):
        arr[lower_area[i][0]][lower_area[i][1]] = ld[i]
    


N, M, T = map(int, input().split())  # 6 이상 r, c는 50이하, t는 1000이하
arr = [list(map(int, input().split())) for _ in range(N)]

t = 0
while t != T:
    dust = []
    blower = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] and arr[i][j] != -1:
                dust.append((i, j, arr[i][j]))
            elif arr[i][j] == -1:
                blower.append((i, j))

    spread(dust)
    upper_area = []
    lower_area = []
    upper_dust = deque()
    lower_dust = deque()
    make_blow_area(blower[0][0], blower[0][1], 'upper', upper_area, upper_dust)
    make_blow_area(blower[1][0], blower[1][1], 'lower', lower_area, lower_dust)
    blow(upper_dust, lower_dust)
    t += 1
    # pprint(arr)

ans = 0
for row in arr:
    ans += sum(row)
print(ans+2)

'''
7 8 2
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
'''