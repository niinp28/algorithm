# 수열의 점수

n = int(input())
minus = []
plus = []
ans = 0
for _ in range(n):
    m = int(input())
    if m > 0:
        plus.append(m)
    else:
        minus.append(m)
minus.sort()
plus.sort(reverse=True)
for i in range(0, len(minus), 2):
    if i == len(minus)-1:
        ans += minus[i]
    else:
        ans += minus[i] * minus[i+1]

for i in range(0, len(plus), 2):
    if i == len(plus)-1:
        ans += plus[i]
    else:
        if plus[i] == 1 or plus[i+1] == 1:
            ans += plus[i]
            ans += plus[i+1]
        else:
            ans += plus[i] * plus[i+1]

print(ans)