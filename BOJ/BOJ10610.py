# 30

num = list(map(int, input()))
num.sort(reverse=True)
if sum(num) % 3 != 0 or num[-1] != 0:
    print(-1)
else:
    print(''.join(map(str, num)))
