N, K = map(int, input().split())
goods = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
knapsack = [[0] * (K+1) for _ in range(N+1) ]

for i in range(1, N+1):
    for j in range(1, K+1):
        W, V = goods[i][0], goods[i][1]

        # 현재 물건의 무게가 배낭의 허용 무게보다 클 때는 넣지 않기
        if j < W:
            knapsack[i][j] = knapsack[i-1][j]
        # 그렇지 않을 경우
        # 배낭 최대 무게에서 현재 넣을 물건의 무게를 뺀다(j - W)
        # 혹은 물건을 안 넣고 그대로 가지고 간다
        else:
            knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-W] + V)

print(knapsack[N][K])