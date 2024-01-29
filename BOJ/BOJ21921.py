# 블로그

N, X = map(int, input().split())
lst = list(map(int, input().split()))

if max(lst) == 0:
    print('SAD')
else:
    total = sum(lst[0:X])
    v = total
    cnt = 1
    for i in range(X, N):
        v -= lst[i-X]
        v += lst[i]
        if v > total:
            total = v
            cnt = 1
        elif v == total:
            cnt += 1
    print(total)
    print(cnt)

