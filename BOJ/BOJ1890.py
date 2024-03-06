# 점프
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            print(dp[i][j])
            break            
        
        cur = arr[i][j]

        if i + cur < N:
            dp[i+cur][j] += dp[i][j]
        if j + cur < N:
            dp[i][j+cur] += dp[i][j]


'''
4
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0
'''