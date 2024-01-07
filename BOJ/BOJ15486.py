# 퇴사 2
N = int(input())
counsel = [0]
dp = [0] * (N+1)
for _ in range(N):
    t, p = map(int, input().split())
    counsel.append((t, p))

for i in range(1, len(dp)):
    dp[i] = max(dp[i], dp[i-1])
    finish_day = i + counsel[i][0] - 1
    if finish_day <= N:  # 작업 완료날이 퇴사전 마지막날 보다 앞선 시점이면
        dp[finish_day] = max(dp[finish_day], dp[i-1]+counsel[i][1])
print(dp[-1])