# 상어 중학교
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
from collections import deque
def rotate(arr):
    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = arr[j][n-i-1]
    return new_arr

def gravity(arr):
    for r in range(n-1, -1, -1):
        for c in range(n-1, -1, -1):
            if arr[r][c] == -1:
                continue
            else:
                q = deque()
                q.append((r, c))
                while q:
                    x, y = q.popleft()
                    nx = x + dr[1]
                    if nx >=0 and nx < n:
                        if arr[nx][y] == '#':
                            q.append((nx, y))
                            arr[nx][y] = arr[x][y]
                            arr[x][y] = '#'
                        elif arr[nx][y] >= -1:
                            break


def bfs(r, c):
    cnt = 1
    r_cnt = 0
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    rainbows = []
    blocks = []
    blocks.append((r, c))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]
            if (0<=nx<n) and (0<=ny<n):
                if arr[nx][ny] == -1:
                    continue
                elif arr[nx][ny] == arr[r][c] or arr[nx][ny] == 0:
                    if not visited[nx][ny]:
                        if arr[nx][ny] == 0:
                            rainbows.append((nx, ny))
                            r_cnt += 1
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                        blocks.append((nx, ny))
                        cnt += 1

    # 무지개 블록만 방문체크 복원
    for r_block in rainbows:
        a, b = r_block
        visited[a][b] = 0
    
    return cnt, blocks, r_cnt, rainbows

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
ans = 0

while True:
    mx = 0
    r_flag = 0
    selected = []
    for r in range(n):
        for c in range(n):
            if arr[r][c] == '#':
                continue
            if arr[r][c] > 0 and visited[r][c] == 0:
                t_cnt, t_blocks, r_cnt, rainbows = bfs(r, c)
                t_blocks.sort(key=lambda x: (x[0], x[1]))
                if t_cnt == 1:
                    continue
                else:
                    if mx < t_cnt:
                        mx = t_cnt
                        selected = t_blocks
                        r_flag = r_cnt
                    elif mx == t_cnt:
                        if r_flag < r_cnt:
                            selected = t_blocks
                            r_flag = r_cnt
                        elif r_flag == r_cnt:
                            for i in range(len(selected)):
                                if selected[i] not in rainbows:
                                    s_r, s_c = selected[i]
                                    break                                 
                            for i in range(len(t_blocks)):
                                if t_blocks[i] not in rainbows:
                                    t_r, t_c = t_blocks[i]
                                    break  
                            if s_r < t_r:
                                selected = t_blocks[:]
                                r_flag = r_cnt
                            elif s_r == t_r:
                                if s_c < t_c:
                                    selected = t_blocks[:]
                                    r_flag = r_cnt
    if mx <= 1:
        break
    
    # 제거
    ans += mx**2
    for co in selected:
        x, y = co
        arr[x][y] = '#'


    # 1차 중력
    gravity(arr)
    # 90도 반시계 회전 그리고 2차 중력
    new_arr = rotate(arr)
    arr = new_arr[:]
    gravity(arr)
    visited = [[0] * n for _ in range(n)]


print(ans)