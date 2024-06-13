# 케빈 베이컨
from collections import deque

def bfs(s):
    q = deque()
    visited = [0] * (N+1)
    visited[s] = 1
    q.append(s)
    while q:
        cur = q.popleft()
        for neighbor in rel[cur]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = visited[cur] + 1
    return sum(visited)


N, M = map(int, input().split())
rel = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    rel[a].append((b))
    rel[b].append((a))

ans = [0, float('inf')]
for i in range(1, N+1):
    tmp = bfs(i)
    if ans[1] > tmp:
        ans[0] = i
        ans[1] = tmp
print(ans[0])