# 파티

import heapq
def dijkstra(start):
    dist = [float('inf')] * (N+1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cur_d, cur_v = heapq.heappop(pq)

        if cur_d > dist[cur_v]: continue
        for neighbor, weight in g[cur_v]:
            distance = weight + cur_d
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist

N, M, X = map(int, input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    g[u].append((v, w))

ans = 0
for i in range(1, N+1):
    tmp = dijkstra(i)[X] + dijkstra(X)[i]
    if ans < tmp:
        ans = tmp
print(ans)
