# 리모컨

target = int(input())
m = int(input())
ans = abs(100 -  target)
if m:
    broken = set(input().split())
else:
    broken = set()


for num in range(1000000):
    num = str(num)

    for j in num:
        if j in broken:
            break
    
    else:
        ans = min(ans, abs(target-int(num)) + len(num)) 

print(ans)