# 정육점

n, m = map(int, input().split())
meat = [tuple(map(int, input().split())) for _ in range(n)]
meat.sort(key=lambda x: (x[1], -x[0]))
# print(meat)

total_w = 0
same = 0
ans = 1e10

for i in range(n):
    weight, cost = meat[i][0], meat[i][1]

    total_w += weight
    if i > 0 and cost == meat[i-1][1]:
        same += cost
    else:
        same = 0
    
    if total_w >= m:
        ans = min(ans, cost + same)

if ans == 1e10:
    print(-1)
else:
    print(ans)

