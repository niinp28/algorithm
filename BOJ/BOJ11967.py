# 불켜기
from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def bfs(r, c):
    q = deque()
    q.append((r, c))
    lighted[r][c] = 1
    visited[r][c] = 1
    ans = 1
    while q:
        cr, cc = q.popleft()
        if graph.get((cr, cc)):
            for la, lb in graph[(cr, cc)]:
                if not lighted[la][lb]:
                    lighted[la][lb] = 1
                    ans += 1
                    
                    for d in range(4):
                        nr = la + dr[d]
                        nc = lb + dc[d]
                        if (0<=nr<N) and (0<=nc<N) and visited[nr][nc]:
                            q.append((nr, nc))
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if (0<=nr<N) and (0<=nc<N) and not visited[nr][nc] and lighted[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1
    return ans
        

N, M = map(int, input().split())  # 100이하, 20000이하
graph = {}
visited = [[0] * N for _ in range(N)]
lighted = [[0] * N for _ in range(N)]

for _ in range(M):
    x, y, a, b = map(int, input().split())
    graph[(x-1, y-1)] = graph.get((x-1, y-1), []) + [(a-1, b-1)]

print(bfs(0, 0))

'''
3 6
1 1 1 2
2 1 2 2
1 1 1 3
2 3 3 1
1 3 1 2
1 3 2 1
'''