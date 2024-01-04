N, M = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
for i in range(len(lst)-1):
    tmp = lst[i]
    j = i
    while True:
        if lst[j] == M:
            ans += 1
            break
        if j == len(lst)-1:
            break
        
        if tmp + lst[j+1] > M:
            break
        elif tmp + lst[j+1] < M:
            tmp += lst[j+1]
            j += 1
        else:
            ans += 1
            break
if lst[-1] == M:
    ans += 1
print(ans)