# 로봇 조종

N, M = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(N)]

for j in range(1, M):
    dp[0][j] += dp[0][j-1]

for i in range(1, N):
    left_to_right = dp[i][:]
    right_to_right = dp[i][:]

    for j in range(M):
        if j == 0:
            left_to_right[j] += dp[i-1][j]
        else:
            left_to_right[j] += max(left_to_right[j-1], dp[i-1][j])
    for j in range(M-1, -1, -1):
        if j == M-1:
            right_to_right[j] += dp[i-1][j]
        else:
            right_to_right[j] += max(right_to_right[j+1], dp[i-1][j])
    
    for j in range(M):
        dp[i][j] = max(left_to_right[j], right_to_right[j])

print(dp[N-1][M-1])