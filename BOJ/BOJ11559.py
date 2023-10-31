# 뿌요뿌요
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
from collections import deque
def bfs(r, c):

    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    blocks = []
    blocks.append((r, c))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]
            if (0 <= nx < 12) and (0 <= ny < 6) and not visited[nx][ny]:
                if arr[nx][ny] == arr[r][c]:
                    blocks.append((nx, ny))
                    q.append((nx, ny))
                    visited[nx][ny] = 1

    block_areas.append(len(blocks))

    if len(blocks) >= 4:
        for block in blocks:
            br, bc = block
            arr[br][bc] = '.'

def gravity():
    for i in range(11, -1, -1):
        for j in range(5, -1, -1):
            if arr[i][j] == '.':
                continue
            else:
                que = deque()
                que.append((i, j))
                while que:
                    r, c = que.popleft()
                    nr = r + dr[1]
                    if (0 <= nr < 12):
                        if arr[nr][c] == '.':
                            que.append((nr, c))
                        elif arr[nr][c] != '.':
                            if (r, c) != (i, j):
                                arr[r][c] = arr[i][j]
                                arr[i][j] = '.'
                            else:
                                continue
                            
                    else:
                        if (r, c) != (i, j):
                            arr[r][c] = arr[i][j]
                            arr[i][j] = '.'
                        else:
                            continue



arr = [list(input()) for _ in range(12)]
visited = [[0] * 6 for _ in range(12)]
combo = 0


while True:
    bfs_flag = 0
    bomb_flag = 0
    block_areas = []
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.' and not visited[i][j]:
                bfs(i, j)
                bfs_flag += 1

    if not bfs_flag:
        break
    for area in block_areas:
        if area >= 4:
            bomb_flag = 1
    if not bomb_flag:
        break

    gravity()
    combo += 1
    visited = [[0] * 6 for _ in range(12)]

print(combo)