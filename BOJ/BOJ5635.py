# 생일

n = int(input())
tmp_old = ['', 20101231]
tmp_young = ['', 0]
for _ in range(n):
    name, d, m, y = input().split()
    if len(d) < 2:
        d = '0'+ d
    if len(m) < 2:
        m = '0' + m
    info = int(y + m + d)
    
    if tmp_old[1] > info:
        tmp_old[1] = info
        tmp_old[0] = name
    if tmp_young[1] < info:
        tmp_young[1] = info
        tmp_young[0] = name
print(tmp_young[0])
print(tmp_old[0])