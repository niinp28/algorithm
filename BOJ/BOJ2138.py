# 전구와 스위치

N = int(input())
start = input()
lst = list(map(int, start))
goal = list(map(int, input()))
cnt1, cnt2 = 0, 1
ans1, ans2 = 0, 0
for i in range(1, N):
    if goal[i-1] == lst[i-1]:
        continue

    for j in range(i-1, i+2):
        if j < N:
            lst[j] = 1 - lst[j]
    cnt1 += 1
    
if lst == goal:
    ans1 = 1
    

lst = list(map(int, start))
lst[0] = 1 - lst[0]
lst[1] = 1 - lst[1]
for i in range(1, N):
    if goal[i-1] == lst[i-1]:
        continue

    for j in range(i-1, i+2):
        if j < N:
            lst[j] = 1 - lst[j]
    cnt2 += 1
    
if lst == goal:
    ans2 = 1
    


if ans1 and ans2:
    print(min(cnt1, cnt2))
elif ans1 and not ans2:
    print(cnt1)
elif not ans1 and ans2:
    print(cnt2)
else:
    print(-1)
