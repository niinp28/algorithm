# 해킹
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
                heapq.heappush(pq, (distance, neighbor))
    return dist

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split()) # 컴퓨터 개수, 의존성 개수, 컴퓨터 번호
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    res = dijkstra(c)
    cnt = 0
    ans = 0
    for el in res:
        if el != int(1e9):
            cnt += 1
            ans = max(ans, el)
    print(f'{cnt} {ans}')