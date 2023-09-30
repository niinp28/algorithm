# 1로 만들기
N = int(input())
dp = [0] * (N+1)
 
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(1 + dp[i//2], dp[i])
    if i % 3 == 0:
        dp[i] = min(1 + dp[i//3], dp[i])

print(dp[N])