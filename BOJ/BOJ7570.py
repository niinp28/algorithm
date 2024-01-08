# 줄 세우기

n = int(input())
children = [0] + list(map(int, input().split()))
position = [0] * (n+1)
for i in range(1, len(children)):
    position[children[i]] = i

cnt = 1
mx = -1

for i in range(1, len(children)-1):
    if position[i] < position[i+1]:
        cnt += 1
        if cnt > mx:
            mx = cnt
    else:
        mx = max(mx, cnt)
        cnt = 1
print(n-mx if n != 1 else 0)