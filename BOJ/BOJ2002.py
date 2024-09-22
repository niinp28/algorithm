# 추월
from collections import deque
N = int(input())
p1 = deque()
p2 = deque()
cnt = 0

for _ in range(N):
    p1.append(input())
for _ in range(N):
    p2.append(input())

for _ in range(N):
    out = p2.popleft()
    if out != p1[0]:
        p1.remove(out)
        cnt += 1
    else:
        p1.popleft()
print(cnt)