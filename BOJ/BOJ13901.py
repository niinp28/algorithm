# 로봇
dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, -1, 1]
N, M = map(int, input().split())
k = int(input())
arr = [['.'] * M for _ in range(N)]
for _ in range(k):
    a, b = map(int, input().split())
    arr[a][b] = 'x'
sr, sc = map(int, input().split())
arr[sr][sc] = 0

direction = list(map(int, input().split()))
for i in range(len(direction)):
    direction[i] -= 1

di = 0
stack = 0 
while True:
    if stack >= len(direction):
        break
    nr = sr + dr[direction[di]]
    nc = sc + dc[direction[di]]
    if (0<=nr<N) and (0<=nc<M) and arr[nr][nc] == '.':
        arr[nr][nc] = arr[sr][sc] + 1
        sr = nr
        sc = nc
        stack = 0
    else:
        di = (di + 1) % len(direction)
        stack += 1
# print(arr)
print(sr, sc)