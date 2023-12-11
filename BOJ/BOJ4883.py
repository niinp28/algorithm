# 삼각 그래프
tc = 0
while True:
    N = int(input())
    tc += 1
    if not N:
        break
    else:
        arr = [list(map(int, input().split())) for _ in range(N)]
        dp = [[0] * 3 for _ in range(N)]
        dp[0][1] = min(arr[0][1], arr[0][1]+arr[0][0])
        dp[0][2] = arr[0][2] + dp[0][1]
        dp[1][0] = dp[0][1] + arr[1][0]
        for i in range(1, N):
            for j in range(3):
                if i == 1 and not j:
                    continue
                else:
                    if j == 0:
                        dp[i][j] = arr[i][j] + min(dp[i-1][j], dp[i-1][j+1])
                    elif j == 1:
                        dp[i][j] = arr[i][j] + min(dp[i - 1][j], dp[i - 1][j + 1], dp[i-1][j-1], dp[i][j-1])
                    elif j == 2:
                        dp[i][j] = arr[i][j] + min(dp[i - 1][j], dp[i-1][j-1], dp[i][j-1])
        print(f'{tc}. {dp[N-1][1]}')