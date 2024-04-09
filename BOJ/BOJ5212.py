# 지구 온난화

dr = [0,1,0,-1]
dc = [1,0,-1,0]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
sink = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'X':
            cnt = 0
            for d in range(4):
                nr = i + dr[d]
                nc = j + dc[d]
                if 0<=nr<N and 0<=nc<M:
                    if arr[nr][nc] == '.':
                        cnt += 1
                else:
                    cnt += 1
                    
            if cnt >= 3:
                sink.append((i, j))

if sink:
    for r, c in sink:
        arr[r][c] = '.'

r1, r2 = 0, 0
for i in range(N):
    if 'X' in arr[i]:
        r1 = i
        break
for i in range(N-1, -1, -1):
    if 'X' in arr[i]:
        r2 = i
        break
c1, c2 = M-1, 0
for i in range(r1, r2+1):
    for j in range(M):
        if arr[i][j] == 'X':
            c1 = min(c1, j)
            c2 = max(c2, j)

for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print(arr[i][j], end='')
    print()

