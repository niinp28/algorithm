# KCPC

t = int(input())
for _ in range(t):
    n, k, my, logs = map(int, input().split())
    sheet = [[0] * (k+1) for _ in range(n+1)]
    submit = [0] * (n+1)
    time = [0] * (n+1)
    for l in range(logs):
        i, j, s = map(int, input().split())
        sheet[i][j] = max(sheet[i][j], s)
        submit[i] += 1
        time[i] = l
    
    rank = []
    for team in range(1, n+1):
        rank.append((sum(sheet[team]), submit[team], time[team], team))
    rank.sort(key=lambda x: (-x[0], x[1], x[2]))

    for r in range(n):
        if rank[r][3] == my:
            print(r+1)