# 흙길 보수하기

N, L = map(int, input().split())
woongdung = [list(map(int, input().split())) for _ in range(N)]
woongdung.sort()

i = 0
ans = 0

for s, e in woongdung:
    if s > e:
        continue
    if i > s:
        s = i
    
    while s < e:
        s += L
        ans += 1
    i = s
print(ans)