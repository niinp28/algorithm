# 창고 다각형

n = int(input())
pillar = [list(map(int, input().split())) for _ in range(n)]
pillar.sort(key=lambda x: x[0])
ans = 0

s, mx = pillar[0][0], pillar[0][1]
tmp = 0
for i in range(1, len(pillar)):
    pos, h = pillar[i][0], pillar[i][1]

    if h >= mx:
        ans += abs(pos-s) * mx
        mx = h
        tmp = 0
    else:
        tmp = max(tmp, h)

print(ans)