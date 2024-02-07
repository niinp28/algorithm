# 좋다

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 0

for i in range(N):
    tmp = lst[:i] + lst[i+1:]
    s, e = 0, len(tmp)-1
    while s < e:
        total = tmp[s] + tmp[e]
        if total == lst[i]:
            ans += 1
            break
        elif total < lst[i]:
            s += 1
        else:
            e -= 1
print(ans)