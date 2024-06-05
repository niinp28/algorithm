# ABCDE
def dfs(node, cnt):
    global ans
    if cnt > 4:
        ans = 1
        return
    
    visited[node] = 1
    for i in graph[node]:
        if not visited[i]:
            dfs(i, cnt+1)
            visited[i] = 0



N, M = map(int, input().split())
graph = [[] for _ in range(N)]
ans = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    visited = [0] * N
    dfs(i, 1)

print(ans)