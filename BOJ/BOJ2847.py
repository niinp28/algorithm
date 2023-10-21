# 게임을 만든 동준이
N = int(input())
for _ in range(N):
    levels = list(map(int, input().split()))
cnt = 0
for i in range(N-1, 0, -1):
    if levels[i] <= levels[i-1]:
        cnt += (levels[i-1] - levels[i] + 1)
        levels[i-1] = levels[i] - 1

print(cnt)    