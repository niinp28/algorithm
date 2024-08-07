# 빗물

h, w = map(int, input().split())
block = list(map(int, input().split()))
cur = block[0]
block2 = list(enumerate(block))
block2.sort(key=lambda x: x[1])

mx_idx, mx = block2[-1][0], block2[-1][1]
ans = 0
for i in range(1, mx_idx+1):
    if cur > block[i]:
        ans += cur-block[i]
    else:
        cur = block[i]
cur = block[-1]
for j in range(len(block)-1, mx_idx-1, -1):
    if cur > block[j]:
        ans += cur-block[j]
    else:
        cur = block[j]
print(ans)