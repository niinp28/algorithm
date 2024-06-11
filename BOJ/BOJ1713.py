# 후보 추천하기

n = int(input())
r = int(input())
lst = list(map(int, input().split()))
podium = []
cnt = []

for i in lst:
    if i in podium:
        cnt[podium.index(i)] += 1
    else:
        if len(podium) >= n:
            index = cnt.index(min(cnt))
            cnt.pop(index)
            podium.pop(index)
        podium.append(i)
        cnt.append(1)

podium.sort()
print(' '.join(map(str, podium)))