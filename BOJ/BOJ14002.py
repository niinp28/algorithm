# 가장 긴 증가하는 부분 수열 4

n = int(input())
lst = list(map(int, input().split()))
dp = [1] * n
ans = []
for i in range(1, n):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
m = max(dp)
for i in range(n-1, -1, -1):
    if dp[i] == m:
        ans.append(lst[i])
        m -= 1
ans.sort()
print(' '.join(map(str, ans)))