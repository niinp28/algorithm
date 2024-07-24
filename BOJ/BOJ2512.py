# 예산

n = int(input())
money = list(map(int, input().split()))
limit = int(input())

s = 0
e = max(money)
ans = 0
while s <= e:
    m = (s+e) // 2 
    tmp = 0
    for b in money:
        if b <= m:
            tmp += b
        else:
            tmp += m
    
    if tmp <= limit:
        s = m + 1
        ans = m
    else:
        e = m - 1

print(ans)