# 별똥별

N, M, L, K = map(int, input().split())
star = [tuple(map(int, input().split())) for _ in range(K)]
ans = 0
for x1, y1 in star:
    for x2, y2 in star:
        s = 0
        for x, y in star:
            if x1 <= x <= x1+L and y2 <= y <= y2+L:
                s += 1
        ans = max(ans, s)
print(K-ans)
