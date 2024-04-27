# 최단 경로
import heapq

def dijkstra(start):
    dist = [float('inf') for _ in range(V+1)]
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cur_dist, cur_vertex = heapq.heappop(pq)

        if cur_dist > dist[cur_vertex]:
            continue

        for weight, neighbor in graph[cur_vertex]:
            distance = cur_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist
    


V, E = map(int, input().split())
s = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


lst = dijkstra(s)
for i in range(1, len(lst)):
    if type(lst[i]) == int:
        print(lst[i])
    else:
        print('INF')
'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''