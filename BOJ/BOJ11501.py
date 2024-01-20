# 주식

T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    ans = 0
    stock.reverse()
    mx = stock[0]
    for i in range(1, N):
        if mx < stock[i]:
            mx = stock[i]
        else:
            ans += mx-stock[i]
    
    print(ans)