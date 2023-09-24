# 마법사 상어와 비바라기

# 좌, 좌상, 상, 우상, 우, 우하, 하, 좌하
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

def order(d, s):
    global cloud
    # step1, 2. 이동 & 비 내림
    for c in cloud:
        c[0] = (c[0] + dr[d-1] * s) % N
        c[1] = (c[1] + dc[d-1] * s) % N
        arr[c[0]][c[1]] += 1
        visited[c[0]][c[1]] = 1 # step5에서 구름 사라진 칸을 확인하기 위함
    # step3, 4. 물복사, 구름 제거
    for c in cloud:
        r, c = c[0], c[1]
        for d in range(1, 8, 2):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N) or not (0 <= nc < N):
                continue
            else:
                if arr[nr][nc] != 0 :
                    arr[r][c] += 1
    cloud = []
    # step5. 물의 양이 2이상인 모든 칸에 구름 생성, 물의 양 감소
    for r in range(N):
        for c in range(N):
            if arr[r][c] >= 2 and not visited[r][c]:
                cloud.append([r, c])
                arr[r][c] -= 2

    
    


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]

for _ in range(M):
    d, s = map(int, input().split())
    visited = [[0] * N for _ in range(N)]
    order(d, s)

cnt = 0
for r in range(N):
    for c in range(N):
        cnt += arr[r][c]

print(cnt)