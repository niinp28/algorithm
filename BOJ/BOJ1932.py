# 정수 삼각형
n = int(input())
samgak = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = samgak[0][0]
for i in range(1, n):
    for j in range(i+1):
        if i == j:
            dp[i][j] = dp[i-1][j-1] + samgak[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + samgak[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + samgak[i][j]
print(max(dp[n-1]))