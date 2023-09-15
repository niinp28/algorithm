n = int(input())
rooms = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0 

for room in rooms:
    room -= b
    cnt += 1
    if room > 0:
        if room % c:
            cnt += (room // c) + 1
        else:
            cnt += (room // c)

print(cnt)