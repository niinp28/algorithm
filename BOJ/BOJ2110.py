# 공유기 설치

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

s = 1
e = house[-1] - house[0]
ans = 0

while s <= e:
    mid = (s + e) // 2
    now = house[0]
    cnt = 1

    for i in range(1, len(house)):
        if house[i] >= now + mid:
            cnt += 1
            now = house[i]
    
    if cnt >= C:
        s = mid + 1
        ans = mid
    else:
        e = mid - 1

print(ans)
