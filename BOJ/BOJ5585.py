# 거스름돈

yen = int(input())
cnt = 0

change = 1000-yen

while change:
    if change >= 500:
        cnt += change // 500
        change %= 500
    
    elif change >= 100:
        cnt += change // 100
        change %= 100

    elif change >= 50:
        cnt += change // 50
        change %= 50

    elif change >= 10:
        cnt += change // 10
        change %= 10

    elif change >= 5:
        cnt += change // 5
        change %= 5

    elif change >= 1:
        cnt += change // 1
        change %= 1

print(cnt)
