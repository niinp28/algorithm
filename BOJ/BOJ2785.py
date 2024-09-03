# 체인

N = int(input())
chain = list(map(int, input().split()))
chain.sort()

tied = N
idx = 0
ans = 0
smallest = chain[0]

while tied != 1:
    if smallest > 0:
        smallest -= 1
        tied -= 1
        ans += 1
    else:  # 완전 분해
        tied -= 1
        idx += 1
        smallest = chain[idx]
print(ans)