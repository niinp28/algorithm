# 다각형의 면적
N = int(input())
dot = [list(map(int, input().split())) for _ in range(N)]
dot.append(dot[0])
p = 0
m = 0
# 신발끈 정리
for i in range(N):
    p += dot[i][0] * dot[i+1][1]
    m += dot[i][1] * dot[i+1][0]

area = abs(p-m)/2
print(round(area, 1))