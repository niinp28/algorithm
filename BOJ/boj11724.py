# 연결 요소의 갯수
def dfs(n):
    global cnt
    visited[n] = 1
    for node in graph[n]:
        if not visited[node]:
            dfs(node)
        
    
    

n, m = map(int, input().split())
graph = {}
visited = [0] * n
cnt = 0
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1] = graph.get(u-1, []) + [v-1]
    graph[v-1] = graph.get(v-1, []) + [u-1]

for i in range(n):
    if m == 0: break
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)