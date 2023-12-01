# 효율적인 해킹
from collections import deque
def bfs(graph, start):
    visited = [0] * (N+1)
    q = deque()
    q.append(start)
    visited[start] = 1
    cnt = 1
    while q:
        s = q.popleft()
        if graph.get(s) == None:
            break
        else:
            for i in graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1
    return cnt


N, M = map(int, input().split()) # N <= 10,000, M <= 100,000
graph = {}

for _ in range(M):
    a, b = map(int, input().split())
    graph[b] = graph.get(b, []) + [a]

mx = 0
answer = []

for i in range(1, N+1):
    cnt = bfs(graph, i)
    if cnt > mx:
        mx = cnt
        answer = [i]
    elif cnt == mx:
        answer.append(i)

print(' '.join(map(str,answer)))