# 가장 긴 증가하는 부분 수열

N = int(input())
lst = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))