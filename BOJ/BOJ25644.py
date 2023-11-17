# 최대 상승

N = int(input())
lst = list(map(int, input().split()))

buy, sell = lst[0], lst[0]
mx = 0
for i in range(1, N):
    tmp = 0
    if buy > lst[i]:
        buy = lst[i]
        sell = lst[i]
    
    if sell < lst[i]:
        sell = lst[i]
    tmp = abs(buy-sell)

    if tmp >= mx:
        mx = tmp
print(mx)