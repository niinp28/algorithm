# 주유소

N = int(input())
roads = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = 0
selected = price[0]
for i in range(N-1):
    if price[i] < selected:
        selected = price[i]
    ans += selected * roads[i]

print(ans)
    
