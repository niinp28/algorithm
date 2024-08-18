# 덩치

n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n)]
ans = []
for i in range(n):
    w, h = people[i][0], people[i][1]
    tmp = 0
    for j in range(n):
        ww, hh = people[j][0], people[j][1]
        if i == j:
            continue
        else:
            if w < ww and h < hh:
                tmp += 1
    ans.append(tmp+1)
print(' '.join(map(str, ans)))