# 치킨 배달
def cal(chicken):
    global cnt
    total = 0
    for house in houses:
        tmp = float('inf')
        x, y = house
        for chic in chicken:
            r, c = chic
            if tmp > (abs(x-r)+abs(y-c)):
                tmp = abs(x-r)+abs(y-c)
        total += tmp
        if total > cnt:
            return
    if total < cnt:
        cnt = total
        

def choose(level, s, chic):
    if level == m:
        cal(chic_case)
        return 
    else:
        for i in range(s, len(chic)):
            chic_case[level] = chic[i]
            choose(level+1, i+1, chic)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
houses = []
chic_case = [0] * m
chic = []
cnt = float('inf')
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            houses.append((i, j))
        elif arr[i][j] == 2:
            chic.append((i, j))
            arr[i][j] = 0

choose(0, 0, chic)
print(cnt)