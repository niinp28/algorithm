# 상자 넣기

n = int(input())
box = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if box[j] < box[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))