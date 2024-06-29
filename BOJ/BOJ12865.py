# 평범한 배낭

N, K = map(int, input().split())
goods = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

'''
dp[i][w] => i번째 물건까지 고려했을 때, 배낭의 용량이 w일 때의 최대 가치!
'''
for i in range(1, N+1):
    for j in range(1, K+1):
        w, v = goods[i][0], goods[i][1]

        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
            '''
            이전 물건까지 고려했을 때, 배낭의 용량이 j일 때의 최대가치
            VS
            이전 물건까지 고려했을 때, 현재 j무게에서 w만큼 빼준 상태의 최대가치에서 현재 가치를 더한값을 비교한다
            왜 w만큼 빼는가? -> 지금 물건의 무게가 w니까 현재 가치를 더해보려고 지금 물건의 무게만큼 빼주는것
            '''
print(dp[N][K])