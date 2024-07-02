# 내려가기

n = int(input())
dp = [[0] * 3 for _ in range(n)]
dp2 = [[0] * 3 for _ in range(n)]

for i in range(n):
    a, b, c = map(int, input().split())
    if not i:
        dp[i][0] = a
        dp[i][1] = b
        dp[i][2] = c
        dp2[i][0] = a
        dp2[i][1] = b
        dp2[i][2] = c
    else:
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + a
        dp[i][1] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + b
        dp[i][2] = max(dp[i-1][1], dp[i-1][2]) + c
        dp2[i][0] = min(dp2[i-1][0], dp2[i-1][1]) + a
        dp2[i][1] = min(dp2[i-1][0], dp2[i-1][1], dp2[i-1][2]) + b
        dp2[i][2] = min(dp2[i-1][1], dp2[i-1][2]) + c
        

print(max(dp[n-1]), min(dp2[n-1]))