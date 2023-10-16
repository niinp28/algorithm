# 로또
def dfs(level, start):
    if level == 6:
        print(' '.join(map(str, rs)))
    else:
        for i in range(start, len(n)):
            rs[level] = n[i]
            dfs(level+1, i+1)

while True:
    tc = list(map(int, input().split()))
    if tc == [0]:
        break
    else:
        k = tc[0]
        n = tc[1:]
        rs = [0] * 6
        dfs(0, 0)
        print()
    