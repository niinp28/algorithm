# 선 긋기

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

# 1번. 새로운 선분
# 2번. 일부 겹침
# 3번. 아예 포함
ps, pe = -1000000001, -1000000001
total = 0
for line in lst:
    ts, te = line[0], line[1]
    # 1번
    if ts > pe:
        ps = ts
        pe = te
        total += pe-ps

    # 3번. 완전 포함
    if ps <= ts and te <= pe:
        continue

    # 2번. 일부 포함
    if ps <= ts <= pe and te > pe:
        total += te-pe
        pe = te
    
print(total)
