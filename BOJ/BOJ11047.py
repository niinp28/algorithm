N, K = map(int, input().split())
coin = list(int(input()) for _ in range(N))
cnt = 0
for i in range(len(coin)-1, -1, -1):
    if K >= coin[i]:
        cnt += K // coin[i]
        K = K % coin[i]
print(cnt)