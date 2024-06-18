# 행렬

def check(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if A[i][j] == '0':
                A[i][j] = '1'
            else:
                A[i][j] = '0'

N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(N)]
cnt = 0

if (N < 3 or M < 3) and A != B:
    cnt = -1
else:
    for r in range(N-2):
        for c in range(M-2):
            if A[r][c] != B[r][c]:
                cnt += 1
                check(r, c)


if cnt != -1:
    if A != B:
        cnt = -1
print(cnt)
