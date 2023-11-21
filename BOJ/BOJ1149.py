# RGB 거리

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
for i in range(N):
    for j in range(3):
        if i == 0:
            dp[i][j] = costs[i][j]
        else:
            dp[i][j] = costs[i][j] + min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
print(min(dp[-1]))