# CCW
lst = [list(map(int, input().split())) for _ in range(3)]
# 신발끈
ans = (lst[0][0]*lst[1][1] + lst[1][0]*lst[2][1] + lst[2][0]*lst[0][1]) - (lst[1][0]*lst[0][1] + lst[2][0]*lst[1][1] + lst[0][0]*lst[2][1])

if ans > 0:
    print(1) # 반시계
elif ans == 0:
    print(0) # 직선
else:
    print(-1) # 시계
