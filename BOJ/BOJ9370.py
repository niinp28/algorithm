# 미확인 도착지
import heapq
def dijkstra(start):
    dist = [int(1e9)] * (n+1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cur_d, cur_v = heapq.heappop(pq)
        if cur_d >  dist[cur_v]:
            continue
        for neighbor, weight in graph[cur_v]:
            distance = cur_d + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev_vertex[neighbor] = cur_v
                heapq.heappush(pq, (distance, neighbor))
    return dist


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())  #교차로, 도로, 목적지 후보
    s, g, h = map(int, input().split())  # 출발지, gh는 꼭 지나가야하는 도로
    graph = [[] for _ in range(n+1)]
    ans = []
    prev_vertex = [0] * (n+1)
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    ds = dijkstra(s)
    dg = dijkstra(g)
    dh = dijkstra(h)
    for _ in range(t):
        x = int(input())
        if ds[x] == ds[g] + dg[h] + dh[x] or ds[x] == ds[h] + dh[g] + dg[x]:
            ans.append(x)
    
    print(*sorted(ans))