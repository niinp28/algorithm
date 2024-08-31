# 랜선 자르기

N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]

s = 1
e = max(lst)
while s <= e:
    mid = (s+e) // 2
    tmp = 0
    for n in lst:
        tmp += n // mid
    
    if tmp < K:
        e = mid - 1
    else:
        s = mid + 1

print(e)
    