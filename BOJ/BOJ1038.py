# 감소하는 수
from itertools import combinations

n = int(input())
ans = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        number = sorted(list(j), reverse=True)
        ans.append(int(''.join(map(str, number))))

ans.sort()
if len(ans) > n:
    print(ans[n])
else:
    print(-1)