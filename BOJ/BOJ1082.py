# 방 번호

n = int(input())
prices = list(map(int, input().split()))
allow = int(input())
dp = [-float('inf') for _ in range(allow+1)]
for i in range(n-1, -1, -1):
    pr = prices[i]
    for j in range(pr, allow+1):
        dp[j] = max(dp[j], i, dp[j-pr]*10 + i)
print(dp[allow])
