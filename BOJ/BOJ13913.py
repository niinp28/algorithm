# 숨바꼭질 4
from collections import deque
def path(x):
    p = []
    tmp = x
    for _ in range(visited[x]):
        p.append(tmp)
        tmp = move[tmp]
    print(' '.join(map(str, p[::-1])))


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        a = q.popleft()
        if a == K:
            return a
        for d in [a-1, a+1, a*2]:
            if 0 <= d <= 100000 and not visited[d]:
                q.append(d)
                visited[d] = visited[a] + 1
                move[d] = a
    

N, K = map(int, input().split())
visited = [0] * (100001)
move = [0] * (100001)

a = bfs(N)
print(visited[K]-1)
path(a)
