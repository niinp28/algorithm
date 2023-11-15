# 감시 피하기
# 백트래킹 문제 같음
# 주어진 조건의 숫자가 낮음.
# 빈칸에 3개의 장애물을 놓는 경우의 수가 매우 많을 것이므로 가지치기가 필요할 것이라 생각됨.
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def dfs():
    pass

def obs_case(level, start):
    if level == 3:
        dfs()

    else:
        for i in range(start, len(X)):
            arr[X[i][0]][X[i][1]] = 'O'
            obs_case(level+1, i+1)
            arr[X[i][0]][X[i][1]] = 'X'
    


N = int(input())
arr = [list(input().split()) for _ in range(N)]


X = []
T = []
ans = 'NO'
# 빈자리 좌표 담기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'X':
            X.append((i, j))
        if arr[i][j] == 'T':
            T.append((i, j))

obs_case(0, 0)
print(ans)