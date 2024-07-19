# MooTube
'''
from collections import deque
def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [0] * (N+1)
    visited[start] = 1
    u_candidate = [0] * (N+1)
    while q:
        present, mn = q.popleft()
        for nxt, usado in graph[present]:
            if not visited[nxt]:
                visited[nxt] = 1
                q.append((nxt, usado))
                u_candidate[nxt] = min(usado, mn)
    return u_candidate

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for i in range(1, N+1):
    c = bfs(i)
    for j in range(len(c)):
        if c[j] != 0:
            if len(graph[i]) < N-1:
                graph[i].append((j, c[j]))
            else:
                break
# print(graph)            

for _ in range(Q):
    K, V = map(int, input().split())
    ans = 0
    for a, b in graph[V]:
        if b >= K:
            ans += 1
    print(ans)
'''
# 시간 초과남

# MooTube
from collections import deque
def bfs(start, k):
    ans = 0
    q = deque()
    visited = [0] * (N+1)
    visited[start] = 1
    for nxt, usado in graph[start]:
        visited[nxt] = 1
        q.append((nxt, usado))
    
    while q:
        present, kk = q.popleft()
        if kk >= k:
            ans += 1
            for nxt, usado in graph[present]:
                if not visited[nxt]:
                    visited[nxt] = 1
                    q.append((nxt, min(usado, kk)))
    return ans
                
    

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

total = [i for i in range(1, N+1)]
for _ in range(Q):
    K, V = map(int, input().split())
    ans = 0
    print(bfs(V, K))
'''
원래는 graph에 새로운 유사도를 전부 집어 넣은 뒤에 K 이상의 유사도를 가진 
정점의 갯수를 for문으로 찾았지만 시간 초과 엔딩.
bfs 로직 자체에서 갯수를 세도록 변경하는 방법으로 수정
--> 모든 정점을 탐색하면서 현재 정점의 유사도가 기준에 부합하는지 검사
--> 큐에 정점과 현재까지의 유사도 최솟값을 넣어서 탐색하는 방식
'''