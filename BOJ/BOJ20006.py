# 랭킹전 대기열

p, m = map(int, input().split())
rooms = []
for _ in range(p):
    level, name = input().split()
    level = int(level)
    if not rooms:  # 방 없으면 생성(맨 처음만)
        rooms.append([(level, name)])
        continue
    
    for room in rooms:
        flag = False
        if room[0][0]-10<=level<=room[0][0]+10:
            if len(room) < m:
                room.append((level, name))
                flag = True
                break
    if flag == False:
        rooms.append([(level, name)])

for room in rooms:
    room.sort(key=lambda x: x[1])
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    for player in room:
        print(f'{player[0]} {player[1]}')