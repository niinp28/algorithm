# 감시 피하기
# 백트래킹 문제 같음
# 주어진 조건의 숫자가 낮음.
# 빈칸에 3개의 장애물을 놓는 경우의 수가 매우 많을 것이므로 가지치기가 필요할 것이라 생각됨.
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def dfs():
    for t in T:
        visited = [[0] * N for _ in range(N)]
        for d in range(4):
            x, y = t[0], t[1]
            while True:
                nx, ny = x+dr[d], y+dc[d]
                if (0<=nx<N) and (0<=ny<N):
                    if not visited[nx][ny]:
                        if arr[nx][ny] == 'X' or arr[nx][ny] == 'T':
                            x = nx
                            y = ny
                            visited[nx][ny] = 1
                        elif arr[nx][ny] == 'O':
                            break
                        elif arr[nx][ny] == 'S':
                            return True
                else:
                    break
    return False


def obs_case(level, start):
    global T_flag, F_flag
    if level == 3:
        if dfs() == False:
            F_flag += 1
    else:
        for i in range(start, len(X)):
            arr[X[i][0]][X[i][1]] = 'O'
            obs_case(level+1, i+1)
            arr[X[i][0]][X[i][1]] = 'X'
    


N = int(input())
arr = [list(input().split()) for _ in range(N)]


X = []
T = []
F_flag = 0
# 빈자리 좌표 담기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'X':
            X.append((i, j))
        if arr[i][j] == 'T':
            T.append((i, j))

obs_case(0, 0)
if F_flag:
    print('YES')
else:
    print('NO')