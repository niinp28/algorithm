# 서강그라운드
import heapq
def dijkstra(start):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cur_d, cur_v = heapq.heappop(pq)
        if cur_d > dist[cur_v]:
            continue
        for neighbor, weight in graph[cur_v]:
            distance = weight + cur_d
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist


n, m, r = map(int, input().split())
items = [0] +  list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

mx = 0
for i in range(n):
    lst = dijkstra(i+1)
    tmp = 0
    for j in range(1, n+1):
        if lst[j] <= m:
            tmp += items[j]
    if tmp > mx:
        mx = tmp

print(mx)

