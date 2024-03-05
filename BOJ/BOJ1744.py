# 수 묶기

n = int(input())
plus = []
minus = []
ans = 0

for _ in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else:
        ans += num

plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        ans += plus[i]  # 남은 양수 더하기
    else:
        ans += (plus[i] * plus[i+1])

for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        ans += minus[i]  # 남은 양수 더하기
    else:
        ans += (minus[i] * minus[i+1])

print(ans)
