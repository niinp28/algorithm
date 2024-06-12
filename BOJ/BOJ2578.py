# 빙고
def check():
    tmp = 0
    for r in range(5):
        if arr[r] == [0] * 5:
            tmp += 1
    
    for c in range(5):
        if all(arr[r][c] == 0 for r in range(5)):
            tmp += 1
    
    if all(arr[i][i] == 0 for i in range(5)):
        tmp += 1
    
    if all(arr[i][4-i] == 0 for i in range(5)):
        tmp += 1
    
    return tmp
    


arr = [list(map(int, input().split())) for _ in range(5)]
number = []
for _ in range(5):
    number += list(map(int, input().split()))

cnt = 0
ans = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if number[i] == arr[x][y]:
                arr[x][y] = 0
                cnt += 1
    
    if cnt >= 12:
        ans = check()
        if ans >= 3:
            print(i+1)
            break