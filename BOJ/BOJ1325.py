# 효율적인 해킹
from collections import deque
def bfs(start, visited):
    global cnt
    q = deque()
    q.append(start)
    visited.append(start)
    while q:
        s = q.popleft()
        if graph.get(s) == None:
            break
        else:
            for computer in graph[s]:
                if computer not in visited:
                    visited.append(computer)
                    q.append(computer)
                    cnt += 1


N, M = map(int, input().split()) # N <= 10,000, M <= 100,000
graph = {}
answer = []
for _ in range(M):
    a, b = map(int, input().split())
    graph[b] = graph.get(b, []) + [a]

for i in graph.keys():
    cnt = 0
    bfs(i, [])
    answer.append((i, cnt))
answer.sort(key=lambda x: (-x[1], x[0]))
mx = answer[0][1]
result = []
for com, tmp in answer:
    if tmp == mx:
        result.append(com)
print(' '.join(map(str,result)))
