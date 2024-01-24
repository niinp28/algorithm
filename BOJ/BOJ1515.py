# 수 이어쓰기

n = input()
ans = 0
i = 0
while True:
    ans += 1
    tmp = str(ans)
    for s in tmp:
        if n[i] == s:
            i += 1
            if i >= len(n):
                print(ans)
                exit()

