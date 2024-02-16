# 올림픽

N, K = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]

nations.sort(key=lambda x: (x[1], x[2], x[3]), reverse= True)

idx = [nations[i][0] for i in range(N)].index(K)


for i in range(N):
    if nations[i][1:] == nations[idx][1:]:
        print(i+1)
        break