# 연세 토토
n, m = map(int, input().split())
min_cost = []
for _ in range(n):
    P, L = map(int, input().split())
    cost_list = list(map(int, input().split()))
    cost_list.sort(reverse=True)
    if P < L:
        min_cost.append(1)
    else:
        min_cost.append(cost_list[L-1])
min_cost.sort()
ans = 0
tmp = 0
for c in min_cost:
    tmp += c
    if tmp <= m:
        ans += 1
    else:
        break
print(ans)