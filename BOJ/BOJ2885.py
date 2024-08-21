# 초콜릿 식사

k = int(input())
n = 0
while True:
    if k <= 2 ** n:
        break
    n += 1
ans = 2 ** n

if k == 2 ** n:
    print(k, 0)
else:
    n -= 1
    cut = 1
    while k != 0:
        
        if k >= 2 ** n:
            k -= 2 ** n
            
        else:
            n -= 1
            cut += 1

    print(ans, cut)