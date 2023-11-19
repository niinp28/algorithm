# OX 퀴즈

N = int(input())
for _ in range(N):
    ans = 0
    cnt = 0
    st = input()
    for s in st:
        if s == 'O':
            cnt += 1
            ans += cnt
        else:
            cnt = 0
            ans += cnt
    print(ans)