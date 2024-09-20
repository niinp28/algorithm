# 미로 만들기
dr = [0, 1, 0, -1] # 우 하 좌 상
dc = [1, 0, -1, 0]

N = int(input())
command = input()
r, c = 0, 0
maze = set()
maze.add((0, 0))
d = 1
mn_r = 0
mn_c = 0
mx_r = 0
mx_c = 0

for com in command:
    if com == 'R':
        d = (d + 1) % 4
    elif com == 'L':
        d = (d + 3) % 4
    else: # 전진
        r = r + dr[d]
        c = c + dc[d]
        maze.add((r, c))
        if r <= mn_r:
            mn_r = r
        if r >= mx_r:
            mx_r = r
        if c <= mn_c:
            mn_c = c
        if c >= mx_c:
            mx_c = c
N = mx_r - mn_r + 1
M = mx_c - mn_c + 1
ans = [['#'] * M for _ in range(N)]

for x, y in list(maze):
    ans[x-mn_r][y-mn_c] = '.'

for row in ans:
    print(''.join(row))