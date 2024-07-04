# 가장 큰 정사각형
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
mx = 0
for i in range(N):
    for j in range(M):
        if not i:
            dp[i][j] = arr[i][j]
        else:
            if not j:
                dp[i][j] = arr[i][j]
            else:
                if arr[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        tmp = dp[i][j]
        if mx < tmp:
            mx = tmp
print(mx ** 2)


'''
4 4
0100
0111
1110
0010
'''