# 예산

n = int(input())
lst = list(map(int, input().split()))
budget = int(input())

s, e = 0, max(lst)

while s <= e:
    m = (s + e) // 2
    total = 0
    for city in lst:
        if city > m:
            total += m
        else:
            total += city
    
    if total <= budget:
        s = m+1
    else:
        e = m-1
print(e)