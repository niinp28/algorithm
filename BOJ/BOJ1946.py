# 신입사원

t = int(input())
for _ in range(t):
    n = int(input())
    mems = [tuple(map(int, input().split())) for _ in range(n)]
    mems.sort(key=lambda x: (x[0]))
    top = 0
    ans = 1
    for i in range(1, len(mems)):
        if mems[i][1] < mems[top][1]:
            top = i
            ans += 1
    print(ans)