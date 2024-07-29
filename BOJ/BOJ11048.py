# 이동하기

n, m = map(int, input().split())
dp = [[0] * (m+1)] * (n+1)
candy = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + candy[i-1][j-1]
print(dp[n][m])