# 2 x n 타일링

n = int(input())

dp = [0] * (n+1)
if n == 0:
    print(0)
elif n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = dp[i-2]*2 + dp[i-1]
    print(dp[-1]%10007)
