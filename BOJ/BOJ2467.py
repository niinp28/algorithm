# 용액

n = int(input())
flasks = list(map(int, input().split()))
s, e = 0, len(flasks)-1
mn = 1e10
one, another = s, e
while s < e:
    total = flasks[s] + flasks[e]
    if abs(total) < abs(mn):
        mn = abs(total)
        one, another = s, e

    if total > 0:
        e -= 1
    elif total < 0:
        s += 1
    else:
        break
    
print(flasks[one], flasks[another])