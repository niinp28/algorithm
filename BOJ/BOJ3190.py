from collections import deque

N = int(input())
arr = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    R, C = map(int, input().split())
    arr[R-1][C-1] = 1
L = int(input())
turn_lst = [list(input().split()) for _ in range(L)]

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
r = 0 # 초기 행 좌표
c = 0 # 초기 열 좌표
d = 0 # 방향 인덱스
t = 0 # 걸린 시간
i = 0 # 방향 리스트용 인덱스
q = deque()
q.append((r, c))
while 1:
    r = r + dr[d]
    c = c + dc[d]
    t += 1
    # 충돌 조건
    if r < 0 or c < 0 or r >= N or c >= N or (r, c) in q:
        break
    q.append((r, c))

    # 빈 칸에 전진 : 꼬리를 다시 지운다
    # 사과를 먹을 경우: popleft 필요없이 사과의 표시인 1을 지우고 0을 다시 새긴다.
    if arr[r][c] == 0:
        q.popleft()
    else:
        arr[r][c] = 0

    # 방향 전환 지시
    if t == int(turn_lst[i][0]):
        if turn_lst[i][1] == 'D':
            d = (d + 1) % 4
        else:
            d = (d + 3) % 4
        if i < len(turn_lst) - 1:
            i += 1

print(t)