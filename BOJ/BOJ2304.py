# 창고 다각형

n = int(input())

pillar = []
ans = 0
for i in range(n) :
    a,b = map(int,input().split())
    pillar.append([a,b])
#기둥을 x축 순으로 정렬한다. 
pillar.sort()

#가장 높은 기둥의 번호를 알아낸다. 
i = 0
for l in pillar :
    if l[1] >ans :
        ans = l[1]
        idx = i
    i += 1


h = pillar[0][1]


for i in range(idx) :
    if h < pillar[i+1][1] :
        ans += h * (pillar[i+1][0]-pillar[i][0])
        h = pillar[i+1][1]
    #아니면 그냥 현재면적을 더해준다. 
    else :
        ans += h * (pillar[i+1][0] - pillar[i][0])

h = pillar[-1][1]

for i in range(n-1, idx, -1) :
    if h < pillar[i-1][1] :
        ans += h * (pillar[i][0]-pillar[i-1][0])
        h = pillar[i-1][1]
    else :
        ans += h * (pillar[i][0] - pillar[i-1][0])

print(ans)