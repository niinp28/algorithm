# 우체국

n = int(input())
village = []
total = 0
for _ in range(n):
    a, b = map(int, input().split())
    village.append([a, b])
    total += b

village.sort(key=lambda x: x[0])

cnt = 0
for i in range(n):
    cnt += village[i][1]
    if cnt >= total/2:
        print(village[i][0])
        break