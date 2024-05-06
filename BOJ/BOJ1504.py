# 특정한 최단 경로
import heapq
def dijkstra(start):
    dist = [float('inf')] * (N+1)
    pq = [(0, start)]
    dist[start] = 0

    while pq:
        cur_d, cur_v = heapq.heappop(pq)

        if cur_d > dist[cur_v]: continue
        
        for neighbor, weight in g[cur_v]:
            distance = cur_d + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist


N, E = map(int, input().split())
g = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
v1, v2 = map(int, input().split())

first_dijkstra = dijkstra(1)
case1_dijkstra = dijkstra(v1)
case2_dijkstra = dijkstra(v2)

c1_path = first_dijkstra[v1] + case1_dijkstra[v2] + case2_dijkstra[N]
c2_path = first_dijkstra[v2] + case2_dijkstra[v1] + case1_dijkstra[N]

res = min(c1_path, c2_path)
print(res if res < float('inf') else -1)