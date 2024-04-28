# 최소비용 구하기
import heapq
def dijkstra(start):
    dist = [float('inf') for _ in range(N+1)]
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cur_dist, cur_vertex = heapq.heappop(pq)

        if cur_dist > dist[cur_vertex]:
            continue
        for neighbor, weight in g[cur_vertex]:
            distance = weight + cur_dist
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist

N = int(input())
M = int(input())
g = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    g[s].append((e, w))
start, end = map(int, input().split())

print(dijkstra(start)[end])