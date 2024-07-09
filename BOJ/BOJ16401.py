# 과자 나눠주기

M, N = map(int, input().split())
snacks = list(map(int, input().split()))
s = 1
e = max(snacks)
ans = 0
while s <= e:
    mid = (s+e) // 2
    total = 0

    if mid == 0:
        total = 0
        break

    for snack in snacks:
        if snack >= mid:
            total += (snack // mid)

    if total >= M:
        s = mid + 1
        ans = mid
    else:
        e = mid - 1
print(ans)