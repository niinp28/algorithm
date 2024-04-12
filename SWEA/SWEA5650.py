# 핀볼
import sys, pprint
sys.stdin = open('5650.txt')
dr = [0, 1, 0, -1]  # 우 하 좌 상
dc = [1, 0, -1, 0]
def changeDirection(block, direction):
    if block == 5:
        return (direction+2)%4
    elif block == 4:
        if direction == 2 or direction == 3:
            return (direction+2)%4
        elif direction == 1:
            return 2
        elif direction == 0:
            return 3
    elif block == 3:
        if direction == 1 or direction == 2:
            return (direction+2)%4
        elif direction == 0:
            return 1
        elif direction == 3:
            return 2
    elif block == 2:
        if direction == 1 or direction == 0:
            return (direction+2)%4
        elif direction == 2:
            return 1
        elif direction == 3:
            return 0
    elif block == 1:
        if direction == 0 or direction == 3:
            return (direction+2)%4
        elif direction == 1:
            return 0
        elif direction == 2:
            return 3




def simulation(rr, cc, direction):
    sr, sc = rr, cc
    r = rr
    c = cc
    d = direction
    score = 0
    while True:
        nr = r + dr[d]
        nc = c + dc[d]

        if (0<=nr<N) and (0<=nc<N):
            if (nr, nc) == (sr, sc):
                break
            if arr[nr][nc] == -1:
                break

            if 1 <= arr[nr][nc] <= 5:
                nd = changeDirection(arr[nr][nc], d)
                score += 1
                r = nr
                c = nc
                d = nd
            elif 6 <= arr[nr][nc] <= 10:
                if (nr, nc) == wormhole[arr[nr][nc]][0]:
                    nr, nc = wormhole[arr[nr][nc]][1]
                elif (nr, nc) == wormhole[arr[nr][nc]][1]:
                    nr, nc = wormhole[arr[nr][nc]][0]
                r = nr
                c = nc
            else:
                r = nr
                c = nc
        else:
            d = (d+2)%4
            score += 1
            if (r, c) == (sr, sc):
                break
            if 1<=arr[r][c]<=5:
                score += 1
                d = changeDirection(arr[r][c], d)
            elif 6 <= arr[r][c] <= 10:
                if (r, c) == wormhole[arr[r][c]][0]:
                    r, c = wormhole[arr[r][c]][1]
                elif (r, c) == wormhole[arr[r][c]][1]:
                    r, c = wormhole[arr[r][c]][0]


    return score
    


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    wormhole = {}
    mx = 0
    for i in range(N):
        for j in range(N):
            if 6 <= arr[i][j] <= 10:
                wormhole[arr[i][j]] = wormhole.get(arr[i][j], []) + [(i, j)]
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                for d in range(4):
                    tmp = simulation(i, j, d)
                    if mx < tmp:
                        mx = tmp
    
    
    print(f'#{tc} {mx}')

    
