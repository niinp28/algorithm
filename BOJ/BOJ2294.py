# 동전 2

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [10001] * (k+1)
dp[0] = 0

# dp[n] = 가진 동전들로 n원을 만들었을 때 최소 동전 갯수


for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)


if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])