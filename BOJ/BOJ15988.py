# 피보나치수의 확장
dp = [1, 2, 4, 7]
t = int(input())
length = len(dp)
for _ in range(t):
    n = int(input())
    while n > length:
        nxt = (dp[length-3] + dp[length-2] + dp[length-1]) % 1000000009
        dp.append(nxt)
        length += 1
    print(dp[n-1])