from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    visited[v] = True
    q = deque([v])
    while q:
        vertex = q.popleft()
        print(vertex, end=' ')
        for i in graph[vertex]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
        


dfs(v)
print()
visited = [0] * (n+1)
bfs(v)