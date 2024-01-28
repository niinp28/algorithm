# 진우의 달 여행

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0,0,0]  for _ in range(M)] for _ in range(N)]
ans = 1e9

for i in range(N):
    if not i:
        for j in range(M):
            for d in range(3):
                dp[i][j][d] = arr[i][j]

    else:
        for j in range(M):
            if j == 0:
                dp[i][j][0] = arr[i][j] + min(dp[i-1][j+1][1], dp[i-1][j+1][2])
                dp[i][j][1] = arr[i][j] + dp[i-1][j][0]
            elif j == M-1:
                dp[i][j][1] = arr[i][j] + dp[i-1][j][2]
                dp[i][j][2] = arr[i][j] + min(dp[i-1][j-1][0], dp[i-1][j-1][1])
            else:
                dp[i][j][0] = arr[i][j] + min(dp[i-1][j+1][1], dp[i-1][j+1][2])
                dp[i][j][1] = arr[i][j] + min(dp[i-1][j][0], dp[i-1][j][2])
                dp[i][j][2] = arr[i][j] + min(dp[i-1][j-1][0], dp[i-1][j-1][1])

for i in range(M):
    ans = min(min(dp[N-1][i]), ans)
print(ans)