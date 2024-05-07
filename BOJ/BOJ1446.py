# 지름길
import heapq
def dijkstra(start):
    dist = [float('inf')] * (D+1)
    pq = [(0, start)]
    while pq:
        cur_d, cur_v = heapq.heappop(pq)

        if cur_d > dist[cur_v]:
            continue

        for neighbor, weight in g[cur_v]:
            distance = weight + cur_d
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist


N, D = map(int, input().split())
g = [[] for _ in range(D+1)]
for i in range(D):
    g[i].append((i+1, 1))
for _ in range(N):
    a, b, c = map(int, input().split())
    if b > D:
        continue
    g[a].append((b, c))

print(dijkstra(0)[D])
